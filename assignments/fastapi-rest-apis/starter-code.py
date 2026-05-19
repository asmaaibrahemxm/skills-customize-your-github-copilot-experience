from typing import Dict, List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task Manager API")


class TaskInput(BaseModel):
    title: str
    completed: bool = False


tasks: List[Dict] = [
    {"id": 1, "title": "Review FastAPI basics", "completed": False},
    {"id": 2, "title": "Build first endpoint", "completed": False},
]


@app.get("/")
def home() -> Dict[str, str]:
    return {"message": "Welcome to your FastAPI Task Manager!"}


@app.get("/tasks")
def list_tasks() -> List[Dict]:
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int) -> Dict:
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks")
def create_task(task_input: TaskInput) -> Dict:
    new_id = max((task["id"] for task in tasks), default=0) + 1
    new_task = {
        "id": new_id,
        "title": task_input.title,
        "completed": task_input.completed,
    }
    tasks.append(new_task)
    return new_task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_input: TaskInput) -> Dict:
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = task_input.title
            task["completed"] = task_input.completed
            return task
    raise HTTPException(status_code=404, detail="Task not found")
