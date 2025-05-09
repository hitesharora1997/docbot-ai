VENV_NAME = .venv
PYTHON = $(VENV_NAME)/bin/python
PIP = $(VENV_NAME)/bin/pip
DOCKER_IMAGE_NAME = docbot-ai
UVICORN_APP = app.main:app

.PHONY: all setup install run test ingest ui clean docker docker-build docker-run help

all: clean setup install ingest run

setup:
	@echo " Creating virtual environment..."
	python3 -m venv $(VENV_NAME)
	$(PIP) install --upgrade pip

install:
	@echo " Installing dependencies..."
	$(PIP) install -r requirements.txt

run:
	@echo " Starting FastAPI backend in background..."
	@nohup $(VENV_NAME)/bin/uvicorn $(UVICORN_APP) --host 0.0.0.0 --port 8000 > backend.log 2>&1 &
	@echo "️ Launching Streamlit frontend..."
	streamlit run ui/streamlit_app.py

ui:
	@echo "️ Launching Streamlit UI..."
	PYTHONPATH=$(PWD) streamlit run ui/streamlit_app.py

ingest:
	@echo "📥 Chunking and embedding documents..."
	PYTHONPATH=$(PWD) $(PYTHON) scripts/ingest_documents.py

test:
	@echo "✅ Running unit tests..."
	$(PYTHON) -m pytest tests

clean:
	@echo "🧹 Cleaning up environment and bytecode..."
	rm -rf $(VENV_NAME)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -rf {} +

docker-build:
	@echo "🐳 Building Docker image..."
	docker build -t $(DOCKER_IMAGE_NAME) .

docker-run:
	@echo "🐋 Running Docker container..."
	docker run -it --rm -p 8000:8000 --env-file .env $(DOCKER_IMAGE_NAME)

docker: docker-build docker-run

help:
	@echo "Usage: make [TARGET]"
	@echo ""
	@echo "Targets:"
	@echo "  setup           - Create virtual environment"
	@echo "  install         - Install dependencies"
	@echo "  run             - Start FastAPI backend"
	@echo "  ui              - Launch Streamlit UI"
	@echo "  ingest          - Chunk and embed documents into ChromaDB"
	@echo "  test            - Run all unit tests"
	@echo "  clean           - Remove venv and __pycache__"
	@echo "  docker-build    - Build Docker image"
	@echo "  docker-run      - Run Docker container"
	@echo "  docker          - Build and run Docker"
	@echo "  help            - Show this help message"
