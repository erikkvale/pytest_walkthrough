"""
Test the task data type
"""

from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__=(None, None, False, None)


def test_asdict():
    """
    asdict() should return a dictionary
    """
    t_task = Task('do something', 'kvale', True, 21)
    t_dict = t_task._asdict()
    expected = {
        'summary': 'do something',
        'owner': 'kvale',
        'done': True,
        'id': 21
    }
    assert t_dict == expected


def test_replace():
    """
    replace() should change passed in fields
    """
    t_before = Task('finish book', 'Erik', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'Erik', True, 10)
    assert t_after == t_expected

