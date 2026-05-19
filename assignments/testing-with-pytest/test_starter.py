from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


module_path = Path(__file__).with_name("starter-code.py")
spec = spec_from_file_location("starter_code", module_path)
starter_code = module_from_spec(spec)
spec.loader.exec_module(starter_code)

add_task = starter_code.add_task
complete_task = starter_code.complete_task
get_open_tasks = starter_code.get_open_tasks


def test_add_task_creates_task_with_next_id():
    tasks = [{"id": 1, "title": "Read docs", "completed": False}]
    created = add_task(tasks, "Write tests")

    assert created["id"] == 2
    assert created["title"] == "Write tests"
    assert created["completed"] is False
    assert len(tasks) == 2


# TODO: Add more tests for empty titles, missing IDs, and open task filtering.
# Suggested function names:
# - test_add_task_rejects_empty_title
# - test_complete_task_marks_task_completed
# - test_complete_task_raises_for_missing_id
# - test_get_open_tasks_returns_only_incomplete_tasks
