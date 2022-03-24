from queue import Queue, Node 
# import pytest

"""

Can successfully enqueue into a queue
Can successfully enqueue multiple values into a queue
Can successfully dequeue out of a queue the expected value
Can successfully peek into a queue, seeing the expected value
Can successfully empty a queue after multiple dequeues
Can successfully instantiate an empty queue
Calling dequeue or peek on empty queue raises exception
  
  """
  
def test_enqueue():
  queue=Queue()
  queue.enqueue("zaid")
  queue.enqueue("raneem")
  queue.enqueue("raghad")

  actual = queue.last.value
  expected = "raghad"

  #  actual = queue.front.value
  # expected = "zaid"
  
  assert actual == expected
  
  
