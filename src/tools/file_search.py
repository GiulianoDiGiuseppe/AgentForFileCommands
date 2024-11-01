import os
from langchain.agents import tool
from src.utils.logger_utils import logger

"""
File Search Module.

This module provides various functions for searching files based on different criteria, such as 
file name, content, and modification date. It uses the logger to provide detailed output during 
the search operations.
"""


@tool
def search_file(path: str, filename: str) -> str:
    """Searches for a specific file by name within a given directory and returns
    its path if found."""
    logger.debug(f"Starting search for file '{filename}' in directory: {path}")
    for root, _, files in os.walk(path):  # Unused 'dirs' variable replaced with '_'
        if filename in files:
            found_path = os.path.join(root, filename)
            logger.info(f"Found file '{filename}' at: {found_path}")
            return found_path
    logger.warning(f"File '{filename}' not found in '{path}'.")
    return None


@tool
def search_file_by_content(path: str, keyword: str) -> list:
    """Finds all files containing a specified keyword in their content within a
    given directory."""
    found_files = []
    logger.debug(
        f"Starting search for files containing keyword '{keyword}' in directory: {path}"
    )
    for root, _, files in os.walk(path):  # Unused 'dirs' variable replaced with '_'
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                with open(
                    file_path, "r", encoding="utf-8", errors="ignore"
                ) as file:  # Specified encoding
                    if keyword in file.read():
                        found_files.append(file_path)
            except (
                IOError,
                OSError,
            ) as e:  # Specific exceptions instead of general Exception
                logger.error(f"Error reading file '{file_path}': {e}")
    logger.info(f"Found files containing '{keyword}': {found_files}")
    return found_files


@tool
def search_files_by_extension(path: str, extension: str) -> list:
    """Retrieves all files with a specified extension located in a given directory."""
    found_files = []
    logger.debug(
        f"Starting search for files with extension '.{extension}' in directory: {path}"
    )
    for root, _, files in os.walk(path):  # Unused 'dirs' variable replaced with '_'
        for filename in files:
            if filename.endswith(f".{extension}"):
                found_files.append(os.path.join(root, filename))
                logger.debug(f"Found file with extension '.{extension}': {filename}")
    logger.info(f"Found files with extension '.{extension}': {found_files}")
    return found_files


@tool
def search_files_modified_after(path: str, timestamp: float) -> list:
    """Identifies files that have been modified after a specified timestamp in a given directory."""
    found_files = []
    logger.debug(
        f"Starting search for files modified after timestamp {timestamp} in directory: {path}"
    )
    for root, _, files in os.walk(path):  # Unused 'dirs' variable replaced with '_'
        for filename in files:
            file_path = os.path.join(root, filename)
            if os.path.getmtime(file_path) > timestamp:
                found_files.append(file_path)
                logger.debug(f"Found file modified after timestamp: {file_path}")
    logger.info(f"Found files modified after timestamp {timestamp}: {found_files}")
    return found_files


@tool
def search_files_containing_keyword_in_name(path: str, keyword: str) -> list:
    """Locates files whose names contain a specified keyword within a given directory."""
    found_files = []
    logger.debug(
        f"Starting search for files containing keyword '{keyword}' in their name in directory: {path}"
    )
    for root, _, files in os.walk(path):  # Unused 'dirs' variable replaced with '_'
        for filename in files:
            if keyword in filename:
                found_files.append(os.path.join(root, filename))
    logger.info(f"Found files containing '{keyword}' in their name: {found_files}")
    return found_files


def get_tools_file_search() -> list:
    """Returns a list of file operation tools."""
    return [
        search_file,
        search_file_by_content,
        search_files_by_extension,
        search_files_containing_keyword_in_name,
        search_files_modified_after,
    ]
