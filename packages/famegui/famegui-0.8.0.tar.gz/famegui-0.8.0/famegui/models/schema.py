import logging
import typing

import fameio.source.schema as fameio
import yaml


def _must_load_yaml_file(file_path: str) -> dict:
    """Helper function to load the content of a YAML file"""
    logging.debug("loading yaml file {}".format(file_path))
    try:
        with open(file_path) as f:
            return yaml.safe_load(f)
    except Exception as e:
        raise RuntimeError("failed to load yaml file '{}'".format(file_path)) from e


class Schema(fameio.Schema):
    """Extends fameio.Schema with the features required for the GUI"""

    def __init__(self, definitions: dict):
        super().__init__(definitions)

    def agent_supports_product(
        self, agent_type: fameio.AgentType, product_name: str
    ) -> bool:
        """Check if the given agent type supports the given product"""
        return self.agent_types[agent_type.name].products.__contains__(product_name)

    def agent_type_from_name(self, name: str) -> fameio.AgentType:
        return super().agent_types[name] if name in super().agent_types else None

    def get_all_agent_types(self) -> typing.List[str]:
        """Return all agent types"""
        return list(super().agent_types.keys())

    @classmethod
    def from_dict(cls, definitions: dict) -> "Schema":
        return super().from_dict(definitions)

    def get_all_products_for_type(self, agent_type: str) -> typing.List[str]:
        """Return all products for the given agent type"""
        return super().agent_types[agent_type].products

    @staticmethod
    def load_yaml_file(file_path: str) -> "Schema":
        """Load (read and parse) a YAML scenario file"""
        logging.info("loading schema from file {}".format(file_path))
        return Schema.from_dict(_must_load_yaml_file(file_path))
