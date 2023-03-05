# Variables
DOCKER_COMPOSE := docker-compose.yaml
DOCKER_COMPOSE_PROJECT_NAME := dagster_flows

# Targets
build:
	docker-compose -f $(DOCKER_COMPOSE) build

up:
	docker-compose -p $(DOCKER_COMPOSE_PROJECT_NAME) -f $(DOCKER_COMPOSE) up -d

down:
	docker-compose -p $(DOCKER_COMPOSE_PROJECT_NAME) -f $(DOCKER_COMPOSE) down

# Variables
PYTHON_FILES := $(shell find . -name "*.py")
PYTHON_VERSION := 3.9

format:
	@echo "Formatting Python code..."
	pip3 install black
	pip3 install isort
	@black $(PYTHON_FILES)
	@isort $(PYTHON_FILES)
	@echo "Done!"

clean:
	@ find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
	@rm -rf *.pyc build dist tests/reports docs/build .pytest_cache .tox .coverage html/