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

