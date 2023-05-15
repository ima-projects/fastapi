# Full-fledged Python API built with FastAPI

Developed a comprehensive Python API utilizing the FastAPI framework. The application implements essential API design principles, such as route configuration, serialization/deserialization techniques, schema validation, and model utilization. The additional integration of SQL databases using Postgres, implementing thorough testing methodologies using pytest, and constructing a seamless CI/CD pipeline with GitHub actions allowed me to build a robust and scalable API while streamlining the development lifecycle for maximum productivity and reliability.

## Table of Contents
- [Business Problem](#business-problem)
  * [Objective](#objective)
  * [Goal](#goal)
- [Data Source](#data-source)
- [Methods](#methods)
- [Tech Stack](#tech-stack)
- [Technical Overview](#technical-overview)
- [Quick Analysis of Results](#quick-analysis-of-results)
  * [Key Findings](#key-findings)
  * [Limitations and Suggestions](#limitations-and-suggestions)
- [Installation: Simplify Your Analysis](#installation-simplify-your-analysis)
  * [Run Locally in Jupyter Notebook](#run-locally-in-jupyter-notebook)


## Tech Stack
- Python: I have developed this API using Python programming language.
- FastAPI: The API is built on top of the FastAPI framework, which provides a high-performance, easy-to-use, modern web development framework for building RESTful APIs in Python.
- PostgresSQL: An open-source object-relational database system. 

```
.
├── alembic
├── app
│   ├── routes.py
│       ├── auth.py
│       ├── post.py
│       ├── user.py
│       └── vote.py
│   ├── main.py
│   └── utils.py
├── config
│   ├── config.ini
│   └── secrets.py
├── tests
│   ├── test_main.py
│   ├── test_routes.py
│   └── test_utils.py
└── README.md
```
