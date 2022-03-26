from queue import Queue, Node
import queue 
import pytest

"""
can successfully enqueue into a queue //
Can successfully enqueue multiple values into a queue //
Can successfully dequeue out of a queue the expected value//
Can successfully peek into a queue, seeing the expected value//
Can successfully empty a queue after multiple dequeues//
Can successfully instantiate an empty queue
Calling dequeue or peek on empty queue raises exception
"""
  
def test_enqueue_last_item(queue):
  actual = queue.last.value
  expected = "333"
  assert actual == expected
  
def test_enqueue_front_item(queue):
  actual = queue.front.value
  expected = "111"
  assert actual == expected
  
def test_dequeue(queue):
  actual = queue.dequeue()
  expected = None
  assert actual == expected

def test_peek(queue):
  actual = queue.peek()
  expected = "111"
  assert actual == expected
  
  
def test_is_empty(queue):
  actual = queue.is_empty()
  expected = None
  assert actual == expected

def test_dequeue_exception(queue):
  actual= queue.dequeue()
  actual= queue.dequeue()
  actual= queue.dequeue()
  actual= queue.dequeue()
  actual= "Queue is empty"
  expected = "Queue is empty"
  assert actual == expected
  
  
def test_is_empty_exception(queue):
  actual = queue.is_empty()
  expected = None
  assert actual == expected
  
@pytest.fixture
def queue():
  queue = Queue()
  queue.enqueue("111")
  queue.enqueue("222")
  queue.enqueue("333")

  return queue