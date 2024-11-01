"""
YAML Configuration Loader.

This module provides functionality to load and parse YAML configuration files.
"""

from typing import Dict, Any
import yaml
from src.utils.logger_utils import logger  # Ensure the path is correct


def load_yaml(file_path: str) -> Dict[str, Any]:
    """
    Reads a YAML file and returns its content as a dictionary.

    :param file_path: Path to the YAML file.
    :return: Dictionary containing the YAML file content.
    :raises FileNotFoundError: If the specified file does not exist.
    :raises yaml.YAMLError: If there is an error parsing the YAML file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:  # Specify encoding
            content = yaml.safe_load(file)
            logger.info("YAML file '%s' loaded successfully.", file_path)
        return content
    except FileNotFoundError:
        logger.error("YAML file not found: %s", file_path)
        raise  # Re-raise the exception to propagate it
    except yaml.YAMLError as e:
        logger.error("Error parsing YAML file '%s': %s", file_path, e)
        raise  # Re-raise the exception to propagate it


# Example usage of the load_yaml function
config = load_yaml("config.yaml")
