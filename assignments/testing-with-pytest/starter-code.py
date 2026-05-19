def add_task(tasks, title):
    if not title or not title.strip():
        raise ValueError("Task title cannot be empty")

    next_id = max((task["id"] for task in tasks), default=0) + 1
    new_task = {"id": next_id, "title": title.strip(), "completed": False}
    tasks.append(new_task)
    return new_task


def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return task
    raise LookupError("Task not found")


def get_open_tasks(tasks):
    return [task for task in tasks if not task["completed"]]
