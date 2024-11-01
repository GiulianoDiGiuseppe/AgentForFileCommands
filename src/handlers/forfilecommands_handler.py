"""Module for handling file command execution.

This module provides functions to execute shell commands and check for command validity.
"""

from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph
from src.agents.executor_agent import create_nodes, AgentState
from src.agents.graph_agent import add_edges_to_graph, add_nodes_to_graph
from src.llm.openai import llm
from src.utils.logger_utils import logger


def execute_command(command: str) -> str:
    """Executes the given shell command and returns the output and error.

    Args:
        command (str): The shell command to be executed.

    Returns:
        tuple: A tuple containing the output and error from the command execution.
    """
    # GRAPH
    file_operations_node, file_search_node, file_utils_node, folder_operations_node = (
        create_nodes(llm)
    )

    workflow = StateGraph(AgentState)

    workflow = add_nodes_to_graph(
        workflow,
        file_operations_node,
        file_search_node,
        file_utils_node,
        folder_operations_node,
    )
    workflow = add_edges_to_graph(workflow)
    graph = workflow.compile()

    log_agents = []

    try:
        for s in graph.stream({"messages": [HumanMessage(content=command)]}):
            if "__end__" not in s:
                log_agents.append(s)
                log_agents.append("------------------")
                logger.debug("%s", s)
                logger.debug("------------------")

        last_agent = log_agents[-4]
        last_response = last_agent[next(iter(last_agent))]["messages"][-1].content
        logger.debug("Last agent response: %s", last_response)
        return last_response, 200

    except (ValueError, TypeError) as e:  # Catch specific exceptions
        logger.error("Error executing command: %s", e)
        return str(e), 400  # Returning a 400 for specific errors

    except (
        RuntimeError,
        KeyError,
    ) as e:  # Example of catching other specific exceptions
        logger.error("Runtime or Key error occurred: %s", e)
        return str(e), 500  # Adjust the error handling as necessary

    except Exception as e:  # Catch any other unexpected exceptions
        logger.error("An unexpected error occurred: %s", e)
        return "An unexpected error occurred.", 500
