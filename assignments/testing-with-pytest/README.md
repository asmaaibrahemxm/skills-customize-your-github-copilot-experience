# 📘 Assignment: Testing Python Programs with Pytest

## 🎯 Objective

Learn how to write automated tests in Python using pytest. You will create test cases for a small task manager module and use test results to verify program behavior.

## 📝 Tasks

### 🛠️ Write Unit Tests for Core Functions

#### Description
Create pytest test functions for the task manager logic in `starter-code.py`.

#### Requirements
Completed program should:

- Create a `test_starter.py` file that imports functions from `starter-code.py`
- Add tests for `add_task(tasks, title)` to verify valid and invalid input
- Add tests for `complete_task(tasks, task_id)` to verify task status updates
- Add tests for `get_open_tasks(tasks)` to verify filtering of incomplete tasks

### 🛠️ Run Tests and Improve Coverage

#### Description
Run pytest, read failures, and improve test quality by covering edge cases.

#### Requirements
Completed program should:

- Run tests with `pytest` and confirm all tests pass
- Add at least one test that checks raised exceptions using `pytest.raises`
- Include at least one test that uses a list with multiple tasks
- Keep tests independent so they can run in any order
