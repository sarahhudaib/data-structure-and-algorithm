from left_join import left_join
import pytest

def test_working_algo(hash_tables):
    hash_table_one = hash_tables
    hash_table_two = {
        'diligent': 'idle',
        'fond': 'averse',
        'guide': 'follow',
        'flow': 'jam',
        'wrath': 'delight',
    }

    assert left_join(hash_table_one, hash_table_two) == {
        'diligent': ['employed\t', 'idle'],
        'fond': ['enamored', 'averse'],
        'guide': ['usher', 'follow'],
        'outfit': ['garb', None],
        'wrath': ['anger', 'delight']
    }


def test_hash_table_one_is_empty():
    hash_table_one = {}
    hash_table_two = {
        "sarah": "Hello",
        "sarah2": "Hello2",
        "sarah3": "Hello3"
    }

    assert left_join(hash_table_one, hash_table_two) == "empty"


def test_hash_table_two_is_none():
    hash_table_one = {
        "sarah": "Hello",
        "sarah2": "Hello2",
        "sarah3": "Hello3"
    }

    hash_table_two = {}

    assert left_join(hash_table_one, hash_table_two) == {
        "sarah": ["Hello", None],
        "sarah2": ["Hello2", None],
        "sarah3": ["Hello3", None]
    }

# ---------------------------------------------------------------
@pytest.fixture
def hash_tables():
    hash_table_one = {
        'diligent': 'employed	',
        'fond': 'enamored',
        'guide': 'usher',
        'outfit': 'garb',
        'wrath': 'anger',
    }

    return hash_table_one