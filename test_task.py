from task import Task
from task_manager import TaskManager

def test_parse_input():
    tm = TaskManager()
    actual = tm.parse_input("+ learn python")
    excepted = ["+","learn python"]
    assert actual == excepted
def test_add():
    tm = TaskManager()
    actual = type(tm.do_action(["+","learn python"]))
    excepted = Task
    assert actual == excepted