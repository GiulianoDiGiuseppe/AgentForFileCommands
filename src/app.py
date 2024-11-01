# main.py
from fastapi import FastAPI
from src.controllers.forfilecommands_controller import router as agent_router

app = FastAPI()

# Include the agent router
app.include_router(agent_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
