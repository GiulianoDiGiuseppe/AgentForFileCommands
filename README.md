# AgentForFileCommands

LLM File System Agent: A Python server that enables an LLM-based agent to execute command-line operations on the file system via a REST API.

## Guide to Clone and Activate a Project with Poetry

* **Open Terminal or Command Prompt**:
* **Clone the Repository**:

  Run the following command, replacing `<repository_url>` with the actual URL of the repository:

  ```bash

  git clone <repository_url>

  cd <repository_name>

  ```
* **Install Dependencies**:

  Install all dependencies listed in `pyproject.toml`:

  ```bash

  poetry install

  ```
* **Activate the Virtual Environment**:

  Activate the Poetry virtual environment:

  ```bash

  poetry shell

  ```

## Run Code

To start the backend, use the following command:

```bash
poetry run python -m uvicorn app:app --reload
```

Once the server is running, you can make POST requests to the following endpoint:  **[http://0.0.0.0:8000/agents](http://0.0.0.0:8000/agents)** .

### Request Body

The body of the request should be formatted as follows:

```
{
    "msg" :    "I want to find all files in directory <PATH_DIRECTORY> with txt extension. Then for those of these files which contain at least 1 word log, change their extension to .log"
}
```

The result will be provided in the response from the last agent.

## Workflow

The system consists of a supervisor agent and four executor agents. The supervisor agent's code can be found in `src/agents/supervisor_agent.py`. Each executor agent has its own set of functions located in `src/tools`.

### Process Overview

1. The supervisor agent receives the initial message.
2. Based on the message, it decides which executor agent should handle the request or sends a "FINISH" message to conclude the workflow.
3. The supervisor monitors the responses from the executor agents and determines whether to continue or halt the process.

This design ensures clear control over the execution flow and allows for effective management of the agents.


# Conclusions

* **Performance Comparison** : The **gpt4o-mini** often created infinite loops and failed to terminate, while **gpt4o** demonstrated significantly higher accuracy.
  * **Improvement Suggestion** : Consider developing an additional agent to refine and clarify the outputs from the executor agents.
  * **Prompt Optimization** : Further optimization of the supervisor agent's prompts could enhance its decision-making capabilities.
* **Agent Organization** : Initially, I tested integrating all tools into a single executor agent. However, I opted to separate the tools into multiple executor agents for better modularity and management.
* **Security Measures** : The current design lacks safeguards against potentially malicious requests and does not incorporate oversight before executing certain actions. Implementing such measures would significantly improve system integrity.
* **Functionality Improvements** : The functions developed are quite basic and present opportunities for optimization:
  * **Enhanced File Search** : Implement recursive searching using functions like `os.walk` to traverse deeper file structures rather than limiting the search to the top level with `os.listdir`.
  * **Path Optimization** : Improve the concatenation of file paths for efficiency and readability.
