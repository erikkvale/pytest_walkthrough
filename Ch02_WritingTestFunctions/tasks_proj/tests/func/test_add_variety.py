import pytest
import tasks
from tasks import Task


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after"""
    # SETUP: start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield # Where the test occurs

    # Teardown: stop db
    tasks.stop_tasks_db()

def equivalent(t1, t2):
    """Check two tasks for equivalence"""
    # Compare everything but the id field
    return (
        (t1.summary == t2.summary) and
        (t1.owner == t2.owner) and
        (t1.done == t2.done)
    )


@pytest.mark.parametrize('task', [
    Task('sleep', done=True),
    Task('wake', 'brian'),
    Task('breathe', 'BRIAN', True),
    Task('exercise', 'BrIaN', False)
])
def test_add_2(task):
    """Demonstrate parameterize with one parameter"""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize(
    'summary, owner, done',
    [
        ('sleep', None, False),
        ('wake', 'brian', False),
        ('breathe', 'BRIAN', True),
        ('eat eggs', 'BrIaN', False),
    ]
)
def test_add_3(summary, owner, done):
    """Demonstrate parametrize with multiple parameters"""
    task = Task(summary, owner, done)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


# Cleaner way of maintaining verbose test info while cleaning the decorator up
tasks_to_try = (
    Task('sleep', done=True),
    Task('wake', 'brian'),
    Task('wake', 'brian'),
    Task('breathe', 'BRIAN', True),
    Task('exercise', 'BrIaN', False),
)

task_ids = [
    'Tasks({},{}.{})'.format(t.summary, t.owner, t.done)
    for t in tasks_to_try
]

@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
def test_add_5(task):
    """Demonstrate ids"""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
class TestAdd:
    """
    Demonstrate parametrize and test classes
    """

    def test_equivalent(self, task):
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert equivalent(t_from_db, task)

    def test_valid_id(self, task):
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert t_from_db.id == task_id