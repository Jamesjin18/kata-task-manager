from task import Task
from task_manager import TaskManager

def test_input():
    tm = TaskManager()
    actual = tm.parse_input("+ python")
    excepted = ["+","python"]
    assert actual == excepted