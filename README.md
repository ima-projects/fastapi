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
- [Continuous Integration and Deployment (CI/CD)](#continuous-integration-and-deployment-cicd)
- [Quick Look of Project in Action](#quick-look-of-project-in-action)
  * [Key Findings](#key-findings)
- [Limitations and Suggestions](#limitations-and-suggestions)
- [Installation](#installation)
  * [Dependencies and Environment Setup](#run-locally-in-jupyter-notebook)

## Business Problem
As the lead developer of a social media company's API project, I have identified that our current technology stack for API development lacks performance, productivity, and scalability. The existing framework is causing maintenance challenges, hindering feature development, and limiting our ability to meet growing user demands effectively.

### Objective
As the lead developer, my objective is to assess the viability of the FastAPI framework for our API project. Through a phased migration approach, I aim to evaluate FastAPI's benefits and capabilities in addressing the limitations of our current technology stack, improving performance, enhancing developer productivity, and enabling future scalability.

### Goal
My primary goal as the lead developer is to assess the viability of the FastAPI framework for our API project and ensure its successful adoption. The specific goals include:
- Viability Assessment: Through phased migration, I will test and evaluate FastAPI's performance, productivity enhancements, and scalability to determine if it meets our requirements and aligns with our long-term goals.
- Seamless Integration: I aim to build an API using FastAPI that seamlessly incorporates the existing CRUD (Create, Read, Update, Delete) methods already being used in our current social media application. This includes ensuring that the data models, endpoints, and functionality are maintained and accessible through the FastAPI-based API.
- Risk Mitigation: As the lead developer, I will carefully plan and execute each phase of the migration to minimize disruption, ensure backward compatibility, and identify and mitigate any potential risks or challenges that may arise during the process, particularly related to the successful integration of CRUD methods. This will be done using a risk assessment.
- Knowledge Transfer and Training: I will share my expertise and provide training to the development team on FastAPI's concepts, best practices, and features to ensure a smooth transition and facilitate the adoption of the new framework while maintaining and enhancing the existing CRUD functionality.

## Methods
- HTTP methods that are commonly used in RESTful APIs (GET, POST, PUT, PATCH and DELETE) including those built with FastAPI, to perform various CRUD (Create, Read, Update, Delete) operations and interact with resources on the server.

## Tech Stack

| Tech      | Description |
| ----------- | ----------- |
| Programming Language | Python: the API is developed using Python programming language. |
| Framework   | FastAPI: the API is built on top of the FastAPI framework, which provides a high-performance, easy-to-use, modern web development framework for building RESTful APIs in Python.  |
| Database Server | PostgresSQL Server: An open-source object-relational database system for data persistence. |

## Technical Overview

This section provides a technical overview of my full-fledged Python API built using the FastAPI framework.

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
 
 ## Continuous Integration and Deployment (CI/CD)
- Continuous Integration 
  * Automated tests using Github Actions
- Deployment 
  * 

## Limitations and Suggestions
### Future suggestions
I will look to include the following: 
- Business Logic and Services: A services.py module which would house the business logic and services that handle the core functionality of the API. It would encapsulate the operations and interactions with data sources or external services.

## Installation
### Dependencies and Environment Setup
