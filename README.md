# Full-fledged Python API built with FastAPI

Developed a comprehensive Python API utilizing the FastAPI framework. The application implements essential API design principles, such as route configuration, serialization/deserialization techniques, schema validation, and model utilization. The additional integration of SQL databases using Postgres, implementing thorough testing methodologies using pytest, and constructing a seamless CI/CD pipeline with GitHub actions allowed me to build a robust and scalable API while streamlining the development lifecycle for maximum productivity and reliability.

## Table of Contents
- [Business Problem](#business-problem)
  * [Objective](#objective)
  * [Goal](#goal)
- [Methods](#methods)
- [Tech Stack](#tech-stack)
- [Technical Overview](#technical-overview)
  * [API Repository Structure](#api-repository-structure)
  * [Key Features and Functionality](#key-features-and-functionality)
- [Quick Look of Project in Action](#quick-look-of-project-in-action)
  * [Key Findings](#key-findings)
- [Limitations and Suggestions](#limitations-and-suggestions)
- [Installation](#installation)
  * [Dependencies and Environment Setup](#run-locally-in-jupyter-notebook)

## Methods
- HTTP methods that are commonly used in RESTful APIs (GET, POST, PUT, PATCH and DELETE) including those built with FastAPI, to perform various CRUD (Create, Read, Update, Delete) operations and interact with resources on the server.

## Tech Stack

| Tech      | Description |
| ----------- | ----------- |
| Programming Language | Python: the API is developed using Python programming language. |
| Framework   | FastAPI: the API is built on top of the FastAPI framework, which provides a high-performance, easy-to-use, modern web development framework for building RESTful APIs in Python.  |
| Database Server | PostgresSQL Server: An open-source object-relational database system for data persistence. |

## Technical Overview

This section provides a technical overview of our full-fledged Python API built using the FastAPI framework.

### API Repository Structure
```
.
├── .vscode
├── alembic
├── app
│   ├── routes.py
│       ├── auth.py
│       ├── post.py
│       ├── user.py
│       └── vote.py
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── main.py
│   ├── oauth2.py
│   ├── schemas.py
│   └── utils.py
├── .gitignore
├── README.md
├── alembic.ini
└── requirements.txt
```
- Main Entry Point: The main.py file serves as the entry point for our API and handles the initialization and configuration of the FastAPI application.
- API Routes and Endpoints: The api.py module defines the various routes and endpoints that our API exposes. It handles incoming requests, performs necessary operations, and returns appropriate responses.
- Data Models and Schemas: The models.py and schema.py file contains the data models and Pydantic schemas respectively. They are used for request and response validation. It ensures data consistency and provides clear contracts for API interactions.

### Key Features and Functionality
- Data Persistence
  * The Python API integrates with a PosgresSQL database or data storage system to persist and retrieve data. 
- Documentation and Testing
  * Included is comprehensive documentation and thorough testing for the success of the API. The API documentation is automatically generated using tools like Swagger UI or ReDoc, providing clear and interactive documentation for API consumers. I followed best practices for unit testing, integration testing, and test coverage to ensure the reliability and stability of our API.
- Deployment and Scalability
  * [add here]
- Continuous Integration and Deployment (CI/CD)
  * 

## Limitations and Suggestions
### Future suggestions
I will look to include the following: 
- Business Logic and Services: A services.py module which would house the business logic and services that handle the core functionality of the API. It would encapsulate the operations and interactions with data sources or external services.

## Installation
### Dependencies and Environment Setup
