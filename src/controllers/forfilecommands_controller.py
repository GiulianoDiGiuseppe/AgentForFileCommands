"""Module for FastAPI controllers handling agent commands.

This module defines endpoints for executing commands via agents and
checks for potentially dangerous commands.
"""

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from src.handlers.forfilecommands_handler import (
    execute_command,
)

from typing import  List
from src.utils.logger_utils import logger

router = APIRouter()


class Message(BaseModel):
    """Model representing a message containing a command."""

    msg: str


command_history: List[str] = []


@router.post(
    "/agent",
    response_model=Message,
    summary="Execute a command via agent",
    description="This endpoint receives a command in a message object and executes it using an agent.",
)
async def agent_command(message: Message):
    """
    Executes a command using the specified agent and returns the output along with the command history.

    - **message**: A JSON object containing the command to be executed in the `msg` field.

    Returns:
        - **output**: A list of log messages generated during the command execution.
        - **error**: Any error messages returned if the command failed.
        - **history**: A list of previous commands executed.

    Raises:
        HTTPException: Raised with a status code of 500 if the command fails to execute.
    """
    logger.info(f"Received command: {message.msg}")  # Log del comando ricevuto

    # Esegui il comando e ottieni output ed errori
    output, status_code = execute_command(message.msg)

    logger.info(
        f"Command execution completed. Output: {output}, Status Code: {status_code}"
    )  # Log dell'esecuzione del comando

    # Controlla se c'è stato un errore
    if status_code != 200:
        logger.error(
            f"Command execution failed with error: {output}"
        )  # Log dell'errore
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Command execution failed with error: {output}",
        )

    return Message(msg=str(output))
