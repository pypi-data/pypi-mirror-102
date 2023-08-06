import unittest
from unittest.mock import MagicMock

from stix.core import STIXPackage, STIXHeader
from src.indicator_bulk_processor import IndicatorBulkProcessor
from src.indicator_enum import URL_TYPE, IPV4_TYPE, IPV6_TYPE, DOMAIN_TYPE, HOSTNAME_TYPE
from tests import create_mock_configuration
from datetime import datetime, timedelta

class IndicatorBulkProcessorTest(unittest.TestCase):

    def setUp(self):
        self.configuration = create_mock_configuration()
        self.indicator = {'type': 'Domain', 'industry_type': ['Tourism', 'Aviation', 'Extremism', 'Adult'], 'ttp': [],
                          'value': 'test.com', 'handling_condition': 'GREEN',
                          'discovered_at': '2021-01-13T18:10:55+0000',
                          'uuid': '3d2c28a8-4a94-43cf-8305-b4e78199aec7', 'description': 'test industry verticals',
                          'source': 'https://test.com/report/incident/69105'}

    def test_add_indicator_without_reaching_the_max_file_size(self):
        indicator_bulk_processor = self._create_bulk_processor_mock()
        indicator_bulk_processor.add(self.indicator)

        self.assertIsNotNone(indicator_bulk_processor.stix_package)
        self.assertEqual(1, indicator_bulk_processor.count)

        indicator_bulk_processor._send.assert_not_called()

    def test_add_indicator_reaching_max_file_size_on_first_call(self):
        indicator_bulk_processor = self._create_bulk_processor_mock()
        indicator_bulk_processor.MAX_INDICATORS_PER_FILE = 1
        indicator_bulk_processor.add(self.indicator)

        self.assertIsNotNone(indicator_bulk_processor.stix_package)
        self.assertEqual(1, indicator_bulk_processor.count)

        indicator_bulk_processor._send.assert_not_called()

    def test_close_with_indicators(self):
        indicator_bulk_processor = self._create_bulk_processor_mock()
        indicator_bulk_processor.add(self.indicator)
        indicator_bulk_processor.add(self.indicator)
        indicator_bulk_processor.close()

        self.assertIsNotNone(indicator_bulk_processor.stix_package)
        self.assertEqual(2, indicator_bulk_processor.count)
        indicator_bulk_processor._send.assert_called()

    def test_close_without_indicator(self):
        indicator_bulk_processor = IndicatorBulkProcessor(self.configuration)
        indicator_bulk_processor._send = MagicMock()
        indicator_bulk_processor.close()
        indicator_bulk_processor._send.assert_not_called()

    def test_url_indicator_to_stix(self):
        indicator = self._create_indicator(URL_TYPE, 'http://wwww.test.com')

        properties = {'type': 'URL', 'value': 'http://wwww.test.com', 'xsi:type': 'URIObjectType'}
        watch_list_type = 'URL Watchlist'
        self._assert_stix_indicator(IndicatorBulkProcessor.parse_indicator_to_stix(indicator), properties,
                                    watch_list_type)

    def test_ipv4_indicator_to_stix(self):
        indicator = self._create_indicator(IPV4_TYPE, '10.1.1.1')

        properties = {'address_value': '10.1.1.1', 'category': 'ipv4-addr', 'xsi:type': 'AddressObjectType'}
        watch_list_type = 'IP Watchlist'
        self._assert_stix_indicator(IndicatorBulkProcessor.parse_indicator_to_stix(indicator), properties,
                                    watch_list_type)

    def test_ipv6_indicator_to_stix(self):
        indicator = self._create_indicator(IPV6_TYPE, '2001:0db8:85a3:0000:0000:8a2e:0370:7334')

        properties = {'address_value': '2001:0db8:85a3:0000:0000:8a2e:0370:7334',
                      'category': 'ipv6-addr', 'xsi:type': 'AddressObjectType'}
        watch_list_type = 'IP Watchlist'
        self._assert_stix_indicator(IndicatorBulkProcessor.parse_indicator_to_stix(indicator), properties,
                                    watch_list_type)

    def test_domain_indicator_to_stix(self):
        indicator = self._create_indicator(DOMAIN_TYPE, 'test.com')

        properties = {'value': 'test.com', 'xsi:type': 'DomainNameObjectType'}
        watch_list_type = 'Domain Watchlist'
        self._assert_stix_indicator(IndicatorBulkProcessor.parse_indicator_to_stix(indicator), properties,
                                    watch_list_type)

    def test_hostname_indicator_to_stix(self):
        indicator = self._create_indicator(HOSTNAME_TYPE, 'www.test.com')

        properties = {'hostname_value': 'www.test.com', 'xsi:type': 'HostnameObjectType'}
        watch_list_type = 'Host Characteristics'
        self._assert_stix_indicator(IndicatorBulkProcessor.parse_indicator_to_stix(indicator), properties,
                                    watch_list_type)

    def test_reindex_indicators_within_thirty_days(self):

        self._create_stix_file()

        indicator_bulk_processor = self._create_bulk_processor_mock()
        indicator_bulk_processor.add(self.indicator)
        indicator_bulk_processor.close()

        self.assertEqual(1, indicator_bulk_processor.count)
        self.assertEqual(2, len(indicator_bulk_processor.stix_package.indicators))
        self.assertCountEqual(['10.1.1.1', 'test.com'],
                              IndicatorBulkProcessorTest._extract_indicator_values(indicator_bulk_processor.stix_package))

        # assert generated stix file
        stix_package_from_xml = STIXPackage.from_xml(self.configuration.get_stix_file_path())
        self.assertEqual(2, len(stix_package_from_xml.indicators))
        self.assertCountEqual(['10.1.1.1', 'test.com'],
                              IndicatorBulkProcessorTest._extract_indicator_values(stix_package_from_xml))

    @staticmethod
    def _extract_indicator_values(stix_package):
        indicators_values = []
        for indicator in stix_package.indicators:
            indicator_dict = indicator.to_dict()
            if indicator_dict['observable']['object']['properties']['xsi:type'] == 'DomainNameObjectType':
                indicators_values.append(indicator_dict['observable']['object']['properties']['value'])
            elif indicator_dict['observable']['object']['properties']['xsi:type'] == 'AddressObjectType':
                indicators_values.append(indicator_dict['observable']['object']['properties']['address_value'])

        return indicators_values

    def _create_stix_file(self):
        # create existing file with indicators older and newer than 30 days
        with open(self.configuration.get_stix_file_path(), 'wb') as stix_file:
            stix_package = STIXPackage(stix_header=STIXHeader())

            older_timestamp = (datetime.now().astimezone() - timedelta(days=40)).replace(microsecond=0).isoformat()
            indicator_url_foo = self._create_indicator(HOSTNAME_TYPE, 'www.foo.com', timestamp=older_timestamp)
            stix_package.add_indicator(IndicatorBulkProcessor.parse_indicator_to_stix(indicator_url_foo))

            indicator_url_one = self._create_indicator(HOSTNAME_TYPE, 'www.one.com', timestamp=older_timestamp)
            stix_package.add_indicator(IndicatorBulkProcessor.parse_indicator_to_stix(indicator_url_one))

            recent_timestamp = datetime.now().astimezone().replace(microsecond=0).isoformat()
            indicator_ip = self._create_indicator(IPV4_TYPE, '10.1.1.1', timestamp=recent_timestamp)

            stix_package.add_indicator(IndicatorBulkProcessor.parse_indicator_to_stix(indicator_ip))
            stix_file.write(stix_package.to_xml())
            stix_file.close()

    def _create_indicator(self, indicator_type, value, timestamp='2021-01-13T18:10:55+00:00'):
        return {'type': indicator_type, 'industry_type': ['Tourism', 'Aviation', 'Extremism', 'Adult'], 'ttp': [],
                'value': value, 'handling_condition': 'GREEN', 'discovered_at': timestamp,
                'uuid': '3d2c28a8-4a94-43cf-8305-b4e78199aec7', 'description': 'test industry verticals',
                'source': 'https://csp.cyjax.com/report/incident/view?id=69105'}

    def _assert_stix_indicator(self, stix_indicator, properties, watch_list_type):
        stix_indicator = stix_indicator.to_dict()

        self.assertEqual('Indicator of compromise', stix_indicator['title'])
        self.assertEqual('test industry verticals', stix_indicator['description'])
        self.assertEqual('3d2c28a8-4a94-43cf-8305-b4e78199aec7', stix_indicator['observable']['id'])
        self.assertEqual('stixVocabs:IndicatorTypeVocab-1.1', stix_indicator['indicator_types'][0]['xsi:type'])
        self.assertEqual('2021-01-13T18:10:55+00:00', stix_indicator['timestamp'])
        self.assertEqual(watch_list_type, stix_indicator['indicator_types'][0]['value'])
        self.assertEqual(properties, stix_indicator['observable']['object']['properties'])

    def _create_bulk_processor_mock(self):
        indicator_bulk_processor = IndicatorBulkProcessor(self.configuration)
        indicator_bulk_processor._send = MagicMock()
        return indicator_bulk_processor
