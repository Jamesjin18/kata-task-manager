from task import Task
from task_manager import TaskManager

def test_parse_input():
    tm = TaskManager()
    actual = tm.parse_input("+ learn python")
    excepted = ["+","learn python"]
    assert actual == excepted
def test_add():
    tm = TaskManager()
    actual = tm.do_action(["+","learn python"])
    excepted = True
    assert actual == excepted
def test_remove():
    tm = TaskManager()
    tm.add_task(Task("1"))
    tm.add_task(Task("2"))
    actual = tm.do_action(["-",3])
    excepted = True
    assert actual == excepted