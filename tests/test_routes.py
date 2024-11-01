import pytest
import os
from httpx import AsyncClient
from src.app import app


@pytest.mark.asyncio
async def test_post_agent_with_valid_payload():
    current_directory = os.getcwd()
    parent_directory = os.path.dirname(current_directory)
    msg = f"I want to find all files in directory '{parent_directory}/src'"
    payload = {"msg": msg}

    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/agent", json=payload)

    assert response.status_code == 200
    response_data = response.json()
    assert "msg" in response_data  # Modifica in base alla tua risposta attesa


@pytest.mark.asyncio
async def test_post_agent_invalid_payload():
    payload = {"invalid_key": "value"}
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/agent", json=payload)

    assert response.status_code == 422  # Unprocessable Entity
