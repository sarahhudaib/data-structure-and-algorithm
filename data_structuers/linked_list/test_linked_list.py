from linked_list import LinkedList, Node 
import pytest

def test_list_creation():
  actual = LinkedList()
  assert actual.head == None
  
def test_empty_linked_list():
    ll = LinkedList()
    assert ll.head == None

def test_multiple_nodes():
    ll = LinkedList()
    sarah = Node("Sarah")
    ahmad = Node("Ahmad")
    hudaib = Node("Hudaib")
    ll.insert(sarah)
    ll.insert(ahmad)
    ll.insert(hudaib)
    assert ll.head.value == 'Hudaib'
    assert ll.head.next.value == 'Ahmad'
    assert ll.head.next.next.value == 'Sarah'
    
def test_insert_method():
  list_insert = LinkedList()
  list_insert.insert(Node(1))
  list_insert.insert(Node(2))
  list_insert.insert(Node(3))

  expected = '  Head-->  3->  2->  1->  None'
  actual = list_insert.ToString()
  assert expected == actual
  

def test_includes_method_if_true():
  list_includes = LinkedList()
  list_includes.append(Node('apples'))
  list_includes.append(Node('oranges'))
  list_includes.insert(Node('strawberries'))
  assert list_includes.includes('oranges') == True

def test_to_string_method():
  list_str = LinkedList()
  list_str.insert(Node(1))
  list_str.append(Node(2))
  list_str.append(Node(3))
  list_str.append(Node(4))
  list_str.append(Node(5))

  actual = list_str.__str__()
  expected = '  Head-->  1->  2->  3->  4->  5->  None'
  assert actual == expected

def test_includes_if_false():
    ll = LinkedList()
    sarah = Node("Sarah")
    ahmad = Node("Ahmad")
    ll.insert(ahmad)
    ll.insert(sarah)
    assert ll.includes('zzzzzzzz') == False

# ----------------------------Extending an Implementation-------------------------------

def test_append_to_the_end():
  list_append = LinkedList()
  list_append.insert(Node('sarah'))
  list_append.append(Node('hudaib'))
  assert list_append.head.next.value == 'hudaib'
  
def test_add_multiple_nodes_to_the_end():
    ll = LinkedList()
    sarah = Node("Sarah")
    ahmad = Node("Ahmad")

    ll.append(sarah)
    ll.append(ahmad)
    assert ll.head.value == 'Sarah'
    assert ll.head.next.value == 'Ahmad'

def test_insert_before_node_located_middle():
    ll = LinkedList()
    sarah = Node("Sarah")
    ahmad = Node("Ahmad")
    ll.append(sarah)
    ll.append(ahmad)
    ll.insert_before("Ahmad", 'Mohammad')
    assert ll.head.next.value == 'Mohammad'
  
def test_insert_before_first_node_in_linked_list():
    ll = LinkedList()
    sarah = Node("Sarah")
    ll.append(sarah)
    ll.insert_before("Sarah", 'Mohammad')
    assert ll.head.value == 'Mohammad'

def test_insert_after_node_in_the_middle():
    ll = LinkedList()
    sarah = Node("Sarah")
    ahmad = Node("Ahmad")
    hudaib = Node("Hudaib")
    ll.append(sarah)
    ll.append(ahmad)
    ll.append(hudaib)
    ll.insert_after("Ahmad", 10001)
    assert ll.head.next.next.value == 10001   

def test_insert_after_last_in_the_linked_list():
    ll = LinkedList()
    sarah = Node("Sarah")
    ahmad = Node("Ahmad")
    hudaib = Node("Hudaib")
    ll.append(sarah)
    ll.append(ahmad)
    ll.append(hudaib)
    ll.insert_after("Hudaib", 10002)
    assert ll.head.next.next.next.value == 10002
    
  # ----------------------------kth_from_end() method tests--------------------------------

# “Happy Path” where k is not at the end, but somewhere in the middle of the linked list
def test_kth_greater_than_the_list():
    ll = LinkedList()
    ll.append(Node(10))
    ll.append(Node(20))
    ll.append(Node(30))
    ll.append(Node(40))
    expected = "k not in the range"
    actual =ll.kth_from_end(6)
    assert expected == actual
        
def test_the_linked_list_size_is_one():
    ll = LinkedList()
    ll.append(Node(10))
    expected = 10
    actual =ll.kth_from_end(0)
    assert expected == actual
    
def test_kth_is_negative_int():
    ll = LinkedList()
    ll.append(Node(10))
    ll.append(Node(20))
    ll.append(Node(30))
    ll.append(Node(40))
    expected = "k not in the range"
    actual =ll.kth_from_end(-2)
    assert expected 
    
def test_kth_and_ll_are_the_same():
    ll = LinkedList()
    ll.append(Node(10))
    ll.append(Node(20))
    ll.append(Node(30))
    ll.append(Node(40))
    expected = 40
    actual =ll.kth_from_end(0)
    assert expected == actual
    
def test_happy_path():
    ll = LinkedList()
    ll.append(Node('Sarah'))
    ll.append(Node('Ahmad'))
    ll.append(Node('Mohammad'))
    ll.append(Node('Hudaib'))
    assert ll.kth_from_end(2) == 'Ahmad' 

  # ----------------------------zip_lists() method tests--------------------------------
linked_list_one = linked_list_two = None
for i in reversed(range(1, 8, 2)):
      linked_list_one = Node(i, linked_list_one)

for i in reversed(range(2, 8, 2)):
      linked_list_two = Node(i, linked_list_two)
      
def test_zip_lists():
  ll = LinkedList()
  actual =ll.zip_lists(linked_list_one, linked_list_two)
  expected = 'After Merge: 1 —> 2 —> 3 —> 4 —> 5 —> 6 —> 7 —> None'
  assert expected == actual
  
# def test_insert_method():
#   list_insert = LinkedList()
#   list_insert.insert(Node(1))
#   list_insert.insert(Node(2))
#   list_insert.insert(Node(3))

#   expected = 'After Merge: 1 —> 2 —> 3 —> 4 —> 5 —> 6 —> 7 —> None'
#   actual = list_insert.ToString()
#   assert expected == actual