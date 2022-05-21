from hashtable import hash_table

def test_create_empty_table():
    new_hash = hash_table(2)
    print(new_hash)
    assert {'size': 2, 'data': [None, None]}
    
def test_set_data():
    new_hash = hash_table(2)
    new_hash.set('one', 1)
    new_hash.set('two', 2)
    new_hash.set('three', 3)
    new_hash.set('four', 4)
    new_hash.set('five', 5)
    print(new_hash)
    assert {'size': 2, 'data': [[['one', 1], ['five', 5]], [['two', 2], ['three', 3], ['four', 4]]]}
    
def test_collision_data ():
    new_hash = hash_table(2)
    new_hash.set('one', 1)
    new_hash.set('eno', 2)
    print(new_hash)
    assert {'size': 2, 'data': [[['one', 1], ['eno', 2]], None]}
    
def test_get_data():
    new_hash = hash_table(2)
    new_hash.get('one')
    new_hash.get('two')
    print(new_hash)
    assert 1,2
    
def test_hash_keys():
    new_hash = hash_table(2)
    new_hash.keys()
    print(new_hash)
    assert ['one', 'five', 'two', 'three', 'four']
    
def test_hash_values():
    new_hash = hash_table(2)
    new_hash.values()
    print(new_hash)
    assert [1, 5, 2, 3, 4]
    
def test_hash_contains():
    new_hash = hash_table(2)
    new_hash.contains('one')
    print(new_hash)
    assert True
    
