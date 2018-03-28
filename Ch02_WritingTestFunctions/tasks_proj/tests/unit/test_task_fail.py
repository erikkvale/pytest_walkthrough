from tasks import Task


def test_task_equality():
    """
    Different tasks should not be equal
    """
    t1 = Task('sit there', 'erik')
    t2 = Task('do something', 'kvale')
    assert t1 == t2


def test_dict_equality():
    """
    Different tasks compared as dicts should not be equal
    """
    t1_dict = Task('make sandwich', 'kvale')._asdict()
    t2_dict = Task('make sandwich', 'kvalem')._asdict()
    assert t1_dict == t2_dict


