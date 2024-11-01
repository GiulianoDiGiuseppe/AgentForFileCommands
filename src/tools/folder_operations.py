"""
Folder Operations Module.

This module provides a set of utilities for managing folders, including creation, 
listing, navigation,
searching, renaming, moving, and copying folders, as well as retrieving folder sizes.
"""

import os
import shutil
from langchain.agents import tool
from src.utils.logger_utils import logger


@tool
def create_folder(path: str, folder_name: str) -> str:
    """Creates a new folder in the specified path."""
    folder_path = os.path.join(path, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    logger.info("Created folder: %s", folder_path)
    return folder_path


@tool
def get_current_folder() -> str:
    """Returns the current working directory."""
    current_folder = os.getcwd()
    logger.info("Current folder: %s", current_folder)
    return current_folder


@tool
def list_folders(path: str) -> list:
    """Returns a list of all folders in the specified directory."""
    folders = [
        item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))
    ]
    logger.info("Folders in '%s': %s", path, folders)
    return folders


@tool
def go_to_parent_folder(path: str) -> str:
    """Returns the absolute path of the parent folder."""
    parent_folder = os.path.abspath(os.path.join(path, ".."))
    logger.info("Parent folder: %s", parent_folder)
    return parent_folder


@tool
def go_to_child_folder(path: str, child_folder: str) -> str:
    """Returns the absolute path of the specified child folder."""
    child_path = os.path.join(path, child_folder)
    if os.path.isdir(child_path):
        logger.info("Child folder: %s", child_path)
        return os.path.abspath(child_path)
    logger.error("Child folder '%s' does not exist in '%s'.", child_folder, path)
    raise FileNotFoundError(
        f"La cartella figlia '{child_folder}' non esiste in '{path}'."
    )


@tool
def search_folder_by_name(path: str, folder_name: str) -> str:
    """Searches for a folder by name in the specified directory and its parent directories,
    returning its path if found."""
    while True:
        if folder_name in os.listdir(path):
            found_path = os.path.join(path, folder_name)
            logger.info("Found folder '%s' at: %s", folder_name, found_path)
            return found_path

        parent_path = os.path.dirname(path)
        if parent_path == path:
            break
        path = parent_path

    logger.warning("Folder '%s' not found in '%s'.", folder_name, path)
    return None


@tool
def count_folders(path: str) -> int:
    """Counts the number of folders in the specified directory and returns the count."""
    folder_count = sum(
        os.path.isdir(os.path.join(path, name)) for name in os.listdir(path)
    )
    logger.info("Number of folders in '%s': %d", path, folder_count)
    return folder_count


@tool
def filter_folders_by_name(path: str, filter_name: str) -> list:
    """Returns a list of folders in the specified directory that contain the filter name."""
    folders = [
        name
        for name in os.listdir(path)
        if os.path.isdir(os.path.join(path, name)) and filter_name in name
    ]
    logger.info(
        "Filtered folders containing '%s' in '%s': %s", filter_name, path, folders
    )
    return folders


@tool
def rename_folder(path: str, old_folder_name: str, new_folder_name: str) -> str:
    """Renames a specified folder in the directory."""
    old_folder_path = os.path.join(path, old_folder_name)
    new_folder_path = os.path.join(path, new_folder_name)
    if os.path.isdir(old_folder_path):
        os.rename(old_folder_path, new_folder_path)
        logger.info(
            "Renamed folder from '%s' to '%s' in '%s'",
            old_folder_name,
            new_folder_name,
            path,
        )
        return new_folder_path
    logger.error("Folder '%s' does not exist in '%s'.", old_folder_name, path)
    raise FileNotFoundError(f"La cartella '{old_folder_name}' non esiste in '{path}'.")


@tool
def move_folder(source_path: str, destination_path: str, folder_name: str) -> str:
    """Moves a folder from the source path to the destination path."""
    source_folder = os.path.join(source_path, folder_name)
    destination_folder = os.path.join(destination_path, folder_name)
    if os.path.isdir(source_folder):
        os.rename(source_folder, destination_folder)
        logger.info("Moved folder from '%s' to '%s'", source_folder, destination_folder)
        return destination_folder
    logger.error("Folder '%s' does not exist in '%s'.", folder_name, source_path)
    raise FileNotFoundError(
        f"La cartella '{folder_name}' non esiste in '{source_path}'."
    )


@tool
def copy_folder(source_path: str, destination_path: str, folder_name: str) -> str:
    """Copies a folder from the source path to the destination path."""
    source_folder = os.path.join(source_path, folder_name)
    destination_folder = os.path.join(destination_path, folder_name)
    if os.path.isdir(source_folder):
        shutil.copytree(source_folder, destination_folder)
        logger.info(
            "Copied folder from '%s' to '%s'", source_folder, destination_folder
        )
        return destination_folder
    logger.error("Folder '%s' does not exist in '%s'.", folder_name, source_path)
    raise FileNotFoundError(
        f"La cartella '{folder_name}' non esiste in '{source_path}'."
    )


@tool
def list_subfolders(path: str) -> list:
    """Returns a list of all subfolders in the specified directory."""
    subfolders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    logger.info("Subfolders in '%s': %s", path, subfolders)
    return subfolders


@tool
def get_folder_size(path: str, folder_name: str) -> int:
    """Returns the total size of the specified folder in bytes."""
    folder_path = os.path.join(path, folder_name)
    if os.path.isdir(folder_path):
        total_size = sum(
            os.path.getsize(os.path.join(folder_path, f))
            for f in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, f))
        )
        logger.info("Total size of folder '%s': %d bytes", folder_name, total_size)
        return total_size
    logger.error("Folder '%s' does not exist in '%s'.", folder_name, path)
    raise FileNotFoundError(f"La cartella '{folder_name}' non esiste in '{path}'.")


def get_tools_folder_operations() -> list:
    """Returns a list of folder operation tools."""
    return [
        create_folder,
        list_folders,
        go_to_parent_folder,
        go_to_child_folder,
        search_folder_by_name,
        count_folders,
        filter_folders_by_name,
        rename_folder,
        move_folder,
        copy_folder,
        list_subfolders,
        get_folder_size,
    ]
