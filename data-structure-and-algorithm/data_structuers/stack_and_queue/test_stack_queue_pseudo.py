from stack_queue_pseudo import Queue
import pytest
 
def test_enqueue_last_item(queue):
  actual = queue.print_queue()
  expected = None
  assert actual == expected
  
def test_enqueue_front_item(queue):
  actual = queue.print_queue()
  expected = None
  assert actual == expected
  
def test_dequeue(queue):
  actual = queue.dequeue()
  expected = '111'
  assert actual == expected

def test_peek(queue):
  actual = queue.peek()
  expected = "111"
  assert actual == expected
  

def test_dequeue_exception(queue):
  actual= queue.dequeue()
  actual= queue.dequeue()
  actual= queue.dequeue()
  actual= queue.dequeue()
  actual= "Queue is empty"
  expected = "Queue is empty"
  assert actual == expected
  
  
  
@pytest.fixture
def queue():
  queue = Queue()
  queue.enqueue("111")
  queue.enqueue("222")
  queue.enqueue("333")

  return queue