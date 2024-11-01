"""Module for performing various file and folder operations.

This module provides functions to create, list, move, copy, rename, and search folders.
"""

import os
import shutil
from typing import List
from langchain.agents import tool
from src.utils.logger_utils import logger


@tool
def write_to_file(path: str, filename: str, content: str) -> str:
    """Writes content to a file, creating it if it doesn't exist."""
    logger.debug(f"Writing to file at: {path}/{filename}")
    logger.info(f"Content: {content}")

    # Create the full file path
    file_path = os.path.join(path, filename)

    # Open the file in write mode ("w") to create it if it doesn't exist
    with open(file_path, "w", encoding="utf-8", errors="ignore") as file:
        file.write(content)  # Write the content to the file

    logger.info(f"Wrote to file: {file_path}")
    return file_path


@tool
def read_file(path: str, filename: str) -> str:
    """Reads content from a file and returns it."""
    logger.debug(f"Reading file from: {path}/{filename}")
    file_path = os.path.join(path, filename)
    if os.path.isfile(file_path):
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            content = file.read()
        logger.info(f"Read from file: {file_path}")
        return content
    logger.error(f"File '{filename}' does not exist in '{path}'.")
    raise FileNotFoundError(f"The file '{filename}' does not exist in '{path}'.")


@tool
def append_to_file(path: str, filename: str, content: str) -> str:
    """Appends content to an existing file."""
    logger.debug(f"Appending to file at: {path}/{filename}")
    file_path = os.path.join(path, filename)
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        file.write(content + "\n")
    logger.info(f"Appended content to file: {file_path}")
    return file_path


@tool
def rename_file(path: str, old_filename: str, new_filename: str) -> str:
    """Renames a file in the specified path."""
    logger.debug(f"Renaming file from {old_filename} to {new_filename} in {path}")
    old_file_path = os.path.join(path, old_filename)
    new_file_path = os.path.join(path, new_filename)
    if os.path.isfile(old_file_path):
        os.rename(old_file_path, new_file_path)
        logger.info(
            f"Renamed file from '{old_filename}' to '{new_filename}' in '{path}'"
        )
        return new_file_path
    logger.error(f"File '{old_filename}' does not exist in '{path}'.")
    raise FileNotFoundError(f"The file '{old_filename}' does not exist in '{path}'.")


@tool
def create_directory(path: str) -> str:
    """Creates a new directory if it doesn't already exist."""
    logger.debug(f"Creating directory at: {path}")
    if not os.path.exists(path):
        os.makedirs(path)
        logger.info(f"Created directory: {path}")
    else:
        logger.warning(f"Directory '{path}' already exists.")
    return path


@tool
def list_files_in_directory(path: str) -> List[str]:
    """Lists all files in a specified directory."""
    logger.debug(f"Listing files in directory: {path}")
    if os.path.isdir(path):
        files = os.listdir(path)
        logger.info(f"Files in directory '{path}': {files}")
        return files
    logger.error(f"Path '{path}' is not a directory.")
    raise NotADirectoryError(f"The path '{path}' is not a directory.")


@tool
def count_files_in_directory(path: str) -> int:
    """Counts the number of files in a specified directory."""
    logger.debug(f"Counting files in directory: {path}")
    if os.path.isdir(path):
        files = os.listdir(path)
        file_count = len(
            [file for file in files if os.path.isfile(os.path.join(path, file))]
        )
        logger.info(f"Number of files in directory '{path}': {file_count}")
        return file_count
    logger.error(f"Path '{path}' is not a directory.")
    raise NotADirectoryError(f"The path '{path}' is not a directory.")


@tool
def file_exists(path: str, filename: str) -> bool:
    """Checks if a specified file exists."""
    logger.debug(f"Checking if file exists: {path}/{filename}")
    file_path = os.path.join(path, filename)
    exists = os.path.isfile(file_path)
    logger.info(f"File '{filename}' exists: {exists}")
    return exists


def get_tools_file_operations() -> List:
    """Returns a list of file operation tools."""
    return [
        append_to_file,
        count_files_in_directory,
        create_directory,
        file_exists,
        list_files_in_directory,
        read_file,
        rename_file,
        write_to_file,
    ]
