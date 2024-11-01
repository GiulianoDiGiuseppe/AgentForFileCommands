# AgentForFileCommands

LLM File System Agent: A Python server that enables an LLM-based agent to execute command-line operations on the file system via a REST API.

## Requirements

- Python 3.7 or later
- Poetry for dependency management
- FastAPI or Flask for the server
- LangChain or LangGraph for creating the agent
- An LLM (e.g., Google AI Studio)

## Setup Instructions

### Step 1: Install Python

1. Download and install Python from the [official website](https://www.python.org/downloads/).
2. Ensure to check the box "Add Python to PATH" during installation.

### Step 2: Install Poetry

1. Open Command Prompt (Win + R, type `cmd`, and hit Enter).
2. Install Poetry by running:
   ```bash
   pip install poetry
   ```
3. Verify the installation with:
   ```bash
   poetry --version
   ```

### Step 3: Clone the Repository

1. Clone your repository using:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

### Step 4: Set Up the Python Environment

1. Initialize a new Poetry project:

   ```bash
   poetry init
   ```

   Follow the prompts to set up your project.
2. Install required dependencies:

   ```bash
   poetry add fastapi uvicorn langchain
   ```



## Agents

We have X agents, Modfier , Searcher , Mover


### Step 5: Create the Main Application File

1. Create a file named `main.py` and add the following code:
   ```python
   from fastapi import FastAPI
   from pydantic import BaseModel
   import subprocess

   app = FastAPI()

   class Message(BaseModel):
       msg: str

   @app.post("/agent")
   async def agent_command(message: Message):
       command = message.msg
       result = subprocess.run(command, shell=True, capture_output=True, text=True)
       return {"output": result.stdout, "error": result.stderr}

   if __name__ == "__main__":
       import uvicorn
       uvicorn.run(app, host="0.0.0.0", port=8000)
   ```

### Step 6: Code Quality Checks

1. Add development dependencies:

   ```bash
   poetry add --dev black pylint mypy
   ```
2. Run code formatting with Black:

   ```bash
   poetry run black .
   ```
3. Run linter with Pylint:

   ```bash
   poetry run pylint main.py
   ```
4. Run type checks with Mypy:

   ```bash
   poetry run mypy main.py
   ```

### Step 7: Run the Server

Start the FastAPI server with:

```bash
poetry run uvicorn main:app --host 0.0.0.0 --port 8000
```

### Step 8: Test the API

You can test your API using Postman or `curl`. For example, using `curl`:

```bash
curl -X POST "http://localhost:8000/agent" -H "Content-Type: application/json" -d "{"msg": "dir"}"
```

### Step 9: Prepare for Submission

1. Commit your changes:

   ```bash
   git add .
   git commit -m "Initial implementation of LLM File System Agent"
   ```
2. Push to GitHub:

   ```bash
   git push origin main
   ```
3. Write a README.md to describe your project.
