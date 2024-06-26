"""This module encapsulates the logic for generating STAC for the sensor metadata standard."""
import pystac

from stac_generator.generator import StacGenerator


class SensorStacGenerator(StacGenerator):
    """STAC generator for sensor data."""

    def __init__(self, data_file, location_file) -> None:
        super().__init__("sensor", data_file, location_file)

    def validate_data(self) -> bool:
        raise NotImplementedError

    def generate_item(self, location: str, counter: int) -> pystac.Item:
        raise NotImplementedError

    def write_items_to_api(self) -> None:
        raise NotImplementedError

    def generate_catalog(self) -> pystac.Catalog:
        raise NotImplementedError

    def generate_collection(self) -> pystac.Collection:
        raise NotImplementedError

    def write_collection_to_api(self) -> None:
        raise NotImplementedError

    def write_to_api(self) -> None:
        raise NotImplementedError

    def validate_stac(self) -> bool:
        raise NotImplementedError
