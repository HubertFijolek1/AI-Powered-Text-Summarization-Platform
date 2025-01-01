# AI-Powered Text Summarization Platform

Welcome to the AI-Powered Text Summarization Platform project. This application demonstrates a comprehensive set of skills including:

- **Python**: FastAPI, Pydantic, pytest
- **REST API Development**
- **Docker & Docker Compose**
- **Continuous Integration/Continuous Deployment (CI/CD)**
- **Integration with Language Models (LLM)**

## Project Structure

- `app/`: Contains the main backend logic (FastAPI, models, routers).
- `tests/`: Contains unit and integration tests.
- `docker/`: Contains Docker-related configuration files.

## Running the Application Locally

1. **Activate the virtual environment** (if using one):
    ```bash
    source .venv/bin/activate
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the FastAPI application**:
    ```bash
    uvicorn app.main:app --reload
    ```

4. **Access the health check endpoint**:
    Visit `http://localhost:8000/health` in your browser or use `curl`:
    ```bash
    curl http://localhost:8000/health
    ```
    Expected response:
    ```json
    {
      "status": "OK"
    }
    ```
## Logging Configuration
This application uses Python's built-in `logging` module for logs. By default, 
logs are printed to the console (`stdout`). You can set the log level by 
defining the `LOG_LEVEL` environment variable (e.g., `DEBUG`, `INFO`, `WARNING`).

Example:
```bash
 export LOG_LEVEL=DEBUG
 uvicorn app.main:app --reload
 ```

You will see additional debug messages in the terminal.

## Running the Application with Docker

Ensure you have Docker and Docker Compose installed on your machine.

1. **Clone the repository**:
    ```bash
    git clone https://github.com/HubertFijolek1/AI-Powered-Text-Summarization-Platform.git
    cd AI-Powered-Text-Summarization-Platform
    ```

2. **Build and run the containers**:
    ```bash
    docker-compose up --build
    ```

3. **Access the application**:
    - Health Check: `http://localhost:8000/health`
    - Interactive API Docs: `http://localhost:8000/docs`