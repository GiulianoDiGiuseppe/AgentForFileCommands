"""Module for defining agent nodes in the workflow graph.

This module contains the definition of agent nodes that interact with various
file operation tools using a language model.
"""

from functools import partial
import operator
from typing import Sequence
from typing_extensions import TypedDict
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.prebuilt import create_react_agent

from src.tools import (
    get_tools_file_operations,
    get_tools_file_search,
    get_tools_file_utils,
    get_tools_folder_operations,
)


class AgentState(TypedDict):
    """Represents the state of an agent in the workflow graph.

    Attributes:
        messages: A sequence of messages exchanged between agents.
        next: A string indicating the next routing target in the graph.
    """

    messages: Sequence[BaseMessage]
    next: str


def agent_node(state: AgentState, agent, name: str) -> dict:
    """Invoke the agent with the current state and return the result.

    Args:
        state: The current state of the agent.
        agent: The agent to invoke.
        name: The name of the agent.

    Returns:
        A dictionary containing the updated messages.
    """
    result = agent.invoke(state)
    return {
        "messages": [HumanMessage(content=result["messages"][-1].content, name=name)]
    }


def create_nodes(llm) -> tuple:
    """Create agent nodes for the workflow.

    Args:
        llm: The language model used to create agents.

    Returns:
        A tuple of partial functions representing different agent nodes.
    """
    file_operations_agent = create_react_agent(llm, tools=get_tools_file_operations())
    file_operations_node = partial(
        agent_node, agent=file_operations_agent, name="FileOperationAgent"
    )

    file_search_agent = create_react_agent(llm, tools=get_tools_file_search())
    file_search_node = partial(
        agent_node, agent=file_search_agent, name="FileSearchAgents"
    )

    file_utils_agent = create_react_agent(llm, tools=get_tools_file_utils())
    file_utils_node = partial(
        agent_node, agent=file_utils_agent, name="FileUtilsAgents"
    )

    folder_operations_agent = create_react_agent(
        llm, tools=get_tools_folder_operations()
    )
    folder_operations_node = partial(
        agent_node, agent=folder_operations_agent, name="FolderOperation"
    )

    return (
        file_operations_node,
        file_search_node,
        file_utils_node,
        folder_operations_node,
    )
