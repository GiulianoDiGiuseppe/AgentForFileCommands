"""Module for managing the supervisor agent in the workflow.

This module defines the supervisor agent that coordinates the workflow
between various worker agents, directing their actions and managing 
conversations.
"""

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from typing import Literal
from pydantic import BaseModel
from src.llm.openai import llm

members = [
    "FileOperationAgent",
    "FileSearchAgents",
    "FileUtilsAgents",
    "FolderOperation",
]


def supervisor_agent(state) -> dict:
    """Manage the workflow between worker agents.

    This function constructs a prompt for the supervisor agent, directing it
    to oversee the conversation among worker agents and to determine the
    next actions based on their responses.

    Args:
        state: The current state of the workflow, containing messages and
               other relevant data.

    Returns:
        A dictionary containing the output of the supervisor agent's
        processing.
    """
    system_prompt = (
        "You are a supervisor responsible for managing a conversation among the "
        f"following workers: {', '.join(members)}. Your role is to facilitate "
        "the discussion, ensuring that each worker performs their assigned task and "
        "provides their results and status updates. Use the provided context to "
        "guide the conversation and make decisions. Once all tasks are complete, "
        "respond with 'FINISH' to indicate the end of the conversation.\n"
    )

    options = ["FINISH"] + members

    class RouteResponse(BaseModel):
        """Represents the next action for the supervisor agent.

        Attributes:
            next: Indicates which member should act next or if the process
                  should finish.
        """

        next: Literal[*options]

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
            (
                "system",
                "After reviewing the conversation above, assess whether all tasks have been completed. "
                "If any worker still needs to take action, indicate who should proceed by selecting from the following options: {options}. "
                "If all tasks are finished, respond with 'END' to conclude the conversation. "
                "For questions about the current folder, respond directly with the folder name and avoid any additional commentary. "
                "Your response should be clear and decisive.",
            ),
        ]
    ).partial(options=str(options), members=", ".join(members))

    supervisor_chain = prompt | llm.with_structured_output(RouteResponse)
    return supervisor_chain.invoke(state)
