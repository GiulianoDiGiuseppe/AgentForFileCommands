"""
Tools Module.

This module provides utility functions for file and folder operations, including:
- File management (copying, moving, renaming, etc.)
- Directory management (listing, creating, deleting, etc.)
- Searching files and folders based on various criteria.
"""

# Import necessary modules and functions

from .file_operations import (
    append_to_file,
    count_files_in_directory,
    create_directory,
    file_exists,
    list_files_in_directory,
    read_file,
    rename_file,
    write_to_file,
    get_tools_file_operations,
)

from .file_search import (
    search_file,
    search_file_by_content,
    search_files_by_extension,
    search_files_containing_keyword_in_name,
    search_files_modified_after,
    get_tools_file_search,
)

from .folder_operations import (
    copy_folder,
    count_folders,
    create_folder,
    filter_folders_by_name,
    get_folder_size,
    go_to_child_folder,
    go_to_parent_folder,
    list_folders,
    list_subfolders,
    move_folder,
    rename_folder,
    search_folder_by_name,
    get_tools_folder_operations,
)

from .file_utils import (
    move_file,
    compress_files_to_zip,
    copy_file,
    delete_file,
    find_files_by_extension,
    get_file_size,
    list_files,
    get_tools_file_utils,
)

# Export functions for use in other modules
__all__ = [
    "get_tools_file_utils",
    "get_tools_file_operations",
    "get_tools_file_search",
    "get_tools_folder_operations",
    "list_files_in_directory",
    "find_files_by_extension",
    "get_file_size",
    "append_to_file",
    "copy_file",
    "delete_file",
    "file_exists",
    "list_files",
    "move_file",
    "read_file",
    "rename_file",
    "write_to_file",
    "search_file",
    "search_file_by_content",
    "search_files_by_extension",
    "search_files_containing_keyword_in_name",
    "search_files_modified_after",
    "compress_files_to_zip",
    "copy_folder",
    "count_files_in_directory",
    "count_folders",
    "create_directory",
    "create_folder",
    "filter_folders_by_name",
    "get_folder_size",
    "go_to_child_folder",
    "go_to_parent_folder",
    "list_folders",
    "list_subfolders",
    "move_folder",
    "rename_folder",
    "search_folder_by_name",
]
