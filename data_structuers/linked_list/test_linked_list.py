from linked_list import LinkedList, Node 

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

# ----------------------------Extending an Implementation--------------------------------

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
    ll.insert_after("Ahmad", 10000)
    assert ll.head.next.next.value == 10000   

def test_insert_after_last_in_the_linked_list():
    ll = LinkedList()
    sarah = Node("Sarah")
    ahmad = Node("Ahmad")
    hudaib = Node("Hudaib")
    ll.append(sarah)
    ll.append(ahmad)
    ll.append(hudaib)
    ll.insert_after("Hudaib", 10000)
    assert ll.head.next.next.next.value == 10000