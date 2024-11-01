# src/llm/openai.py

"""
Module for managing OpenAI Chat models.

This module initializes the OpenAI Chat model using configuration 
settings defined in the configuration utilities.
"""

# Import statements
from langchain_openai import ChatOpenAI

# Ensure the import path for configuration_utils is correct
from src.utils.configuration_utils import config

llm = ChatOpenAI(**config["openai"])
