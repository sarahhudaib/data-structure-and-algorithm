from stacks import Stack
import pytest
"""
Can successfully push onto a stack //
Can successfully push multiple values onto a stack//
Can successfully pop off the stack//
Can successfully empty a stack after multiple pops//
Can successfully peek the next item on the stack//
Can successfully instantiate an empty stack//
Calling pop or peek on empty stack raises exception
"""
def test_push(stack):
  actual = stack.top.value
  expected = 2
  assert actual == expected
  
def test_push_multiple_values(stack):
  actual = stack.top.next.value
  expected = 3
  assert actual == expected
  
def test_pop(stack):
  actual= stack.pop()
  expected =2
  assert actual == expected
  
def test_pop_empty_stack(stack):
  actual= stack.pop()
  actual= stack.pop()
  actual= stack.pop()
  actual= stack.is_empty()
  expected = None
  assert actual == expected
  
def test_pop_exception(stack):
  actual= stack.pop()
  actual= stack.pop()
  actual= stack.pop()
  # actual= stack.pop()
  actual= "Stack is empty!!"
  expected = "Stack is empty!!"
  assert actual == expected

def test_peek_of_stack(stack):
  actual = stack.peek()
  expected = 2
  assert actual == expected

def test_is_empty_stack(stack):
  actual = stack.is_empty()
  expected = None
  assert actual == expected
  

 #decorator
@pytest.fixture
def stack():
  stack = Stack()
  stack.push(5)
  stack.push(3)
  stack.push(2)

  return stack