import pytest
from httpx import AsyncClient
from src.app import app

@pytest.mark.asyncio
async def test_post_agent_with_valid_payload():
    payload = {
        "msg": "I want to find all files in directory 'C:/Users/digig/Desktop/Works/AgentForFileCommands/src'"
    }
    
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
