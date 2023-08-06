"""
The IndicatorBulkProcessor class manages the bulk process to send indicator to Vectra.
It creates a STIX file that contains the indicators to be sent.
"""

import logging
from datetime import datetime
from os import path

from cybox.core import Object
from cybox.core.observable import Observable
from cybox.objects.address_object import Address
from cybox.objects.domain_name_object import DomainName
from cybox.objects.hostname_object import Hostname
from cybox.objects.uri_object import URI
from stix.core import STIXPackage, STIXHeader
from stix.indicator import Indicator, IndicatorType

from src.configuration import Configuration
from src.indicator_enum import URL_TYPE, IPV4_TYPE, IPV6_TYPE, DOMAIN_TYPE, HOSTNAME_TYPE
from src.vectra_client import VectraClient


class IndicatorBulkProcessor:
    """Processes indicators."""

    EXPIRATION_IN_DAYS = 30

    # pylint: disable=too-many-instance-attributes
    def __init__(self, configuration: Configuration):
        self.count = 0
        self.open = False
        self.configuration = configuration
        self.logger = logging.getLogger('cyjax-vectra')
        self.vectra_client = VectraClient(
            configuration.get_vectra_fqdn(),
            configuration.get_vectra_api_key(),
            configuration.get_vectra_threat_feed_id(),
            configuration.get_vectra_ssl_verification()
        )
        self.stix_package = None
        self.stix_file_path = configuration.get_stix_file_path()

    def _create_stix_package(self):
        """
        Creates the STIX package. If the STIX file exist, use it as starting point.
        """
        self.stix_package = STIXPackage(stix_header=STIXHeader())
        if path.exists(self.stix_file_path):
            existing_indicator_count = 0
            # Only use indicators that have not expired yet
            for indicator in STIXPackage.from_xml(self.stix_file_path).indicators:
                time_since_insertion = datetime.now().astimezone().replace(microsecond=0) - indicator.timestamp
                if time_since_insertion.days < self.EXPIRATION_IN_DAYS:
                    self.stix_package.add_indicator(indicator)
                    existing_indicator_count += 1

            self.logger.debug("Existing indicators: %s", existing_indicator_count)

    def add(self, indicator: dict) -> None:
        """
        Adds an indicator to the bulk processor
        :param indicator: The indicator.
        """
        if not self.open:
            self._create_stix_package()
            self.open = True

        self.logger.debug("Adding indicator: %s", indicator['value'])
        self.count += 1
        self.stix_package.add_indicator(self.parse_indicator_to_stix(indicator))

    def close(self) -> None:
        """
        Closes the bulk processor.
        """
        if self.count > 0:
            self._save_file()
            self._send()

    def _save_file(self) -> None:
        """
        Saves the indicators into a STIX file.
        """
        self.logger.info("Found new %s indicators", self.count)
        # Write the STIX package to files
        with open(self.stix_file_path, 'wb') as stix_file:
            stix_file.write(self.stix_package.to_xml())

    def _send(self) -> None:
        """
        Sends the indicators and saves them to a STIX file.
        """
        self.vectra_client.send_indicators(self.stix_file_path)

    @staticmethod
    def parse_indicator_to_stix(indicator: dict) -> Indicator:
        """
        Parses an indicator to stix format.
        @param indicator: The indicator.
        @return The indicator.
        """

        # Create a CyboX Object
        indicator_type = None
        cybox_object = None
        if indicator['type'] == URL_TYPE:
            indicator_type = IndicatorType.TERM_URL_WATCHLIST
            cybox_object = URI(indicator['value'])
            cybox_object.type_ = URI.TYPE_URL
        elif indicator['type'] == IPV4_TYPE or indicator['type'] == IPV6_TYPE:
            indicator_type = IndicatorType.TERM_IP_WATCHLIST
            cybox_object = Address(indicator['value'])
            cybox_object.category = Address.CAT_IPV4 if indicator['type'] == IPV4_TYPE else Address.CAT_IPV6
        elif indicator['type'] == DOMAIN_TYPE:
            indicator_type = IndicatorType.TERM_DOMAIN_WATCHLIST
            cybox_object = DomainName()
            cybox_object.value = indicator['value']
        elif indicator['type'] == HOSTNAME_TYPE:
            indicator_type = IndicatorType.TERM_HOST_CHARACTERISTICS
            cybox_object = Hostname()
            cybox_object.hostname_value = indicator['value']

        stix_indicator = Indicator(timestamp=indicator['discovered_at'])
        stix_indicator.title = 'Indicator of compromise'
        if indicator_type:
            stix_indicator.add_indicator_type(indicator_type)
        if indicator['description']:
            stix_indicator.add_description(indicator['description'])

        observable = Observable(id_=indicator['uuid'])
        observable.object_ = Object(properties=cybox_object)

        stix_indicator.add_observable(observable)

        return stix_indicator
