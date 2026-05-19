# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using the FastAPI framework in Python. You will learn how to create API routes, validate request data, and return clear JSON responses.

## 📝 Tasks

### 🛠️ Build Core API Endpoints

#### Description
Set up a FastAPI app and implement the main endpoints for a simple task manager API.

#### Requirements
Completed program should:

- Create a FastAPI app instance
- Add a `GET /` endpoint that returns a welcome message
- Add a `GET /tasks` endpoint that returns all tasks
- Add a `GET /tasks/{task_id}` endpoint that returns one task by ID

### 🛠️ Add Create and Update Features

#### Description
Use request body models to accept input and update task data in memory.

#### Requirements
Completed program should:

- Define a Pydantic model for task input data
- Add a `POST /tasks` endpoint to create a new task
- Add a `PUT /tasks/{task_id}` endpoint to update an existing task
- Return helpful error messages when a task ID is not found
