"""
File Utilities Module.

This module provides various file manipulation functions, including file compression, 
size retrieval, listing, deletion, copying, moving, and extension-based search.
"""

import os
import zipfile
import shutil
import glob
from langchain.agents import tool
from src.utils.logger_utils import logger


@tool
def get_file_size(path: str, filename: str) -> int:
    """Returns the size of a specified file in bytes."""
    file_path = os.path.join(path, filename)
    if os.path.isfile(file_path):
        size = os.path.getsize(file_path)
        logger.info("Size of file '%s': %d bytes", filename, size)
        return size
    logger.error("File '%s' does not exist in '%s'.", filename, path)
    raise FileNotFoundError(f"Il file '{filename}' non esiste in '{path}'.")


@tool
def compress_files_to_zip(path: str, zip_filename: str) -> str:
    """Compresses all files in the specified directory into a zip archive."""
    zip_path = os.path.join(path, zip_filename)
    with zipfile.ZipFile(zip_path, "w") as zip_file:
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path):
                zip_file.write(item_path, os.path.relpath(item_path, path))
    logger.info("Compressed files into: %s", zip_path)
    return zip_path


@tool
def list_files(path: str) -> list:
    """Returns a list of all files in the specified directory."""
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    logger.info("Files in '%s': %s", path, files)
    return files


@tool
def delete_file(path: str, filename: str) -> str:
    """Deletes the specified file from the given path."""
    file_path = os.path.join(path, filename)
    if os.path.isfile(file_path):
        os.remove(file_path)
        logger.info("Deleted file: %s", file_path)
        return f"File '{filename}' deleted."
    logger.error("File '%s' does not exist in '%s'.", filename, path)
    raise FileNotFoundError(f"Il file '{filename}' non esiste in '{path}'.")


@tool
def copy_file(source_path: str, destination_path: str, filename: str) -> str:
    """Copies a specified file to a new location."""
    source_file = os.path.join(source_path, filename)
    destination_file = os.path.join(destination_path, filename)
    if os.path.isfile(source_file):
        shutil.copy(source_file, destination_file)
        logger.info("Copied file from '%s' to '%s'", source_file, destination_file)
        return destination_file
    logger.error("File '%s' does not exist in '%s'.", filename, source_path)
    raise FileNotFoundError(f"Il file '{filename}' non esiste in '{source_path}'.")


@tool
def find_files_by_extension(path: str, extension: str) -> list:
    """Finds and returns a list of files with the specified extension."""
    search_pattern = os.path.join(path, f"*.{extension}")
    files = glob.glob(search_pattern)
    logger.info("Found files with extension '%s' in '%s': %s", extension, path, files)
    return files


@tool
def move_file(source_path: str, destination_path: str, filename: str) -> str:
    """Moves a specified file to a new location."""
    source_file = os.path.join(source_path, filename)
    destination_file = os.path.join(destination_path, filename)
    if os.path.isfile(source_file):
        shutil.move(source_file, destination_file)
        logger.info("Moved file from '%s' to '%s'", source_file, destination_file)
        return destination_file
    logger.error("File '%s' does not exist in '%s'.", filename, source_path)
    raise FileNotFoundError(f"Il file '{filename}' non esiste in '{source_path}'.")


def get_tools_file_utils() -> list:
    """Returns a list of file operation tools."""
    return [
        get_file_size,
        compress_files_to_zip,
        list_files,
        delete_file,
        copy_file,
        find_files_by_extension,
        move_file,
    ]
