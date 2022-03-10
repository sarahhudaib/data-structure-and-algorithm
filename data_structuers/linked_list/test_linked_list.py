from linked_list import LinkedList

def test_list_creation():
  actual = LinkedList()
  assert actual.head == None

def test_insert_method():
  lst_one = LinkedList()
  lst_one.insert(1)
  lst_one.insert(2)
  lst_one.insert(3)

  assert lst_one.head.value == 1
  assert lst_one.head.next.value == 2
  assert lst_one.head.next.next.value == 3

def test_includes_method():
  lst_two = LinkedList()
  lst_two.insert('apples')
  lst_two.insert('oranges')
  lst_two.insert('strawberries')

  assert lst_two.includes('oranges') == True
  assert lst_two.includes('salt') == False

def test_to_string_method():
  lst_three = LinkedList()
  lst_three.insert(1)
  lst_three.append(2)
  lst_three.append(3)
  lst_three.append(4)
  lst_three.append(5)

  actual = lst_three.__str__()
  expected = '  Head-->  1->  2->  3->  4->  5->  None'
  assert actual == expected

def test_append():
  lst_four = LinkedList()
  lst_four.insert('apple')
  lst_four.append('banana')
  assert lst_four.head.next.value == 'banana'

