# Airflow Demo

## Overview
This project is a demonstration of Apache Airflow for orchestrating and scheduling workflows. It includes examples of common tasks and integrations to help you get started with building your own data pipelines.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)

## Installation

### Prerequisites
- Python 3.x
- [Poetry](https://python-poetry.org/) (a dependency management and packaging tool for Python)
- [Docker](https://www.docker.com/products/docker-desktop/) and [Docker Compose](https://docs.docker.com/compose/)

### Steps
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/airflow-demo.git
    cd airflow-demo
    ```

2. Install Poetry if you haven't already:
    ```sh
    curl -sSL https://install.python-poetry.org | python3 -
    ```

3. Install the project dependencies using Poetry:
    ```sh
    poetry install
    ```

4. (Optional) Activate the virtual environment created by Poetry:
    ```sh
    poetry shell
    ```

## Usage

### Setting up the Environment with Docker Compose

1. Copy the example environment file:
    ```sh
    cp .env.example .env
    ```

2. Start the Airflow services:
    ```sh
    docker-compose up -d
    ```

3. Access the Airflow UI in your browser: http://localhost:8080

### Shutting Down the Environment

To shut down the Airflow services:
```sh
docker-compose down
```

## Features
- **Task Scheduling:** Demonstrates how to schedule tasks using Airflow.
- **DAG Creation:** Example of creating Directed Acyclic Graphs (DAGs) for workflows.
- **Task Dependencies:** Example of setting up task dependencies to ensure correct execution order.
- **Integrations:** Examples of integrating with different services and databases.