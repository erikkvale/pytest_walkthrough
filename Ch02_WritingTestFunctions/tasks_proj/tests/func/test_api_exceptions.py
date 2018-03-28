import pytest
import tasks

def test_add_raises():
    """
    add() should raise an exception
    with wrong type param
    """
    with pytest.raises(TypeError):
        tasks.add(task='not a Task object')


def test_start_tasks_db_raises():
    """
    Make sure unsupported db raises an exception
    """
    with pytest.raises(ValueError) as exc_info:
        tasks.start_tasks_db(r'some/path', 'mysql')
    exc_msg = exc_info.value.args[0]
    assert exc_msg == "db_type must be a 'tiny' or 'mongo'"


@pytest.mark.smoke
def test_list_tasks_raises():
    """list() should raise an exception with wrong type param"""
    with pytest.raises(TypeError):
        tasks.list_tasks(123)


@pytest.mark.get
@pytest.mark.smoke
def test_get_raises():
    """get() should raise an exception with wrong type"""
    with pytest.raises(TypeError):
        tasks.get(task_id='123')
