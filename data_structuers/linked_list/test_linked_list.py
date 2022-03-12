from linked_list import LinkedList, Node 

def test_list_creation():
  actual = LinkedList()
  assert actual.head == None

def test_insert_method():
  list_insert = LinkedList()
  list_insert.insert(Node(1))
  list_insert.insert(Node(2))
  list_insert.insert(Node(3))

  expected = '  Head-->  3->  2->  1->  None'
  actual = list_insert.ToString()
  assert expected == actual
  

def test_includes_method():
  list_includes = LinkedList()
  list_includes.append(Node('apples'))
  list_includes.append(Node('oranges'))
  list_includes.insert(Node('strawberries'))

  assert list_includes.includes('oranges') == True
  assert list_includes.includes('salt') == False
  

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

def test_append():
  list_append = LinkedList()
  list_append.insert(Node('apple'))
  list_append.append(Node('banana'))
  assert list_append.head.next.value == 'banana'


