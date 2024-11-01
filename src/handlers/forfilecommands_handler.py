"""Module for handling file command execution.

This module provides functions to execute shell commands and check for command validity.
"""

import subprocess
from src.utils.logger_utils import logger
from langgraph.graph import END, StateGraph, START
from langgraph.prebuilt import create_react_agent
from src.agents.node_agent import create_nodes, AgentState
from src.agents.graph_agent import add_edges_to_graph, add_nodes_to_graph
from src.llm.openai import llm
from langchain_core.messages import BaseMessage, HumanMessage


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
                logger.debug(s)
                logger.debug("------------------")
        last_agent = log_agents[-4]
        last_response = last_agent[next(iter(last_agent))]["messages"][-1].content
        logger.debug(f"Last agent response {last_response}")
        return last_response, 200
    except Exception as e:
        logger.error(f"Error executing command: {e}")
        return str(e), 500
