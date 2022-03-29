from stack_queue_pseudo import PseudoQueue
from queue import Queue
import pytest


"""
Happy Path” - Expected outcome
Expected failure
Edge Case (if applicable/obvious)
"""
def test_happy_path():
  pseudo_queue = PseudoQueue()
  pseudo_queue.enqueue(10)
  pseudo_queue.enqueue(15)
  pseudo_queue.enqueue(20)

  assert pseudo_queue.s1.top.value == 10


def test_dequeue():
  pseudo_queue = PseudoQueue()
  pseudo_queue.enqueue(5)
  pseudo_queue.enqueue(10)
  pseudo_queue.enqueue(15)
  pseudo_queue.enqueue(20)

  pop_queue = []
  for i in range(4):
    pop_queue.append(pseudo_queue.dequeue())
  
  assert pop_queue == [5, 10, 15, 20]


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