# core/llm.py
from langchain_openai import ChatOpenAI

from src.utils.configuration_utils import config

llm = ChatOpenAI(**config["openai"])
