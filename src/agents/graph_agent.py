"""Module for managing workflow graphs in file operations using agents."""

from langgraph.graph import END, START  # Importing only what is necessary
from .supervisor_agent import members, supervisor_agent


def add_nodes_to_graph(
    workflow,
    file_operations_node,
    file_search_node,
    file_utils_node,
    folder_operations_node,
):
    """Add nodes representing various agents to the workflow graph.

    Args:
        workflow: The workflow graph to which nodes will be added.
        file_operations_node: The node for file operations.
        file_search_node: The node for file search operations.
        file_utils_node: The node for file utility functions.
        folder_operations_node: The node for folder operations.

    Returns:
        The updated workflow graph with added nodes.
    """
    workflow.add_node("FileOperationAgent", file_operations_node)
    workflow.add_node("FileSearchAgents", file_search_node)
    workflow.add_node("FileUtilsAgents", file_utils_node)
    workflow.add_node("FolderOperation", folder_operations_node)
    workflow.add_node("Supervisor", supervisor_agent)
    return workflow


def add_edges_to_graph(workflow):
    """Add edges to the workflow graph based on member relationships.

    Args:
        workflow: The workflow graph to which edges will be added.

    Returns:
        The updated workflow graph with added edges.
    """
    for member in members:
        # Workers report back to the supervisor when done
        workflow.add_edge(member, "Supervisor")

    # The supervisor populates the "next" field in the graph state
    # which routes to a node or finishes
    conditional_map = {k: k for k in members}
    conditional_map["FINISH"] = END
    workflow.add_conditional_edges("Supervisor", lambda x: x["next"], conditional_map)

    # Finally, add entrypoint
    workflow.add_edge(START, "Supervisor")
    return workflow
