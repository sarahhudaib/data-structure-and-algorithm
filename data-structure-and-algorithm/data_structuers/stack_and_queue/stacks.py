class Node :
  """Linked Lists are made of nodes. So we create a node class.
     It will contain the data and the pointer to the next node."""
  def __init__(self,value):
    self.value=value
    self.next=None 

class Stack :
  """It will consist of a constructor having the top pointer, i.e., 
  the pointer which points to the top element of the stack at any given time"""
  def __init__(self,node=None):
    self.top = node 

  def push(self,value):
    """Next comes the push operation, where we insert an element at the top of the stack"""
    node = Node(value)
    node.next = self.top
    self.top = node 

  def pop(self) :
    """Next comes the pop operation where we remove the top element from the stack"""
    try:
      if self.top != None:
        temp = self.top
        self.top = self.top.next
        temp.next= None
      return temp.value
    except:  
      raise Exception("Stack is empty!!")

  def peek(self):
    """The peek method will allow us to peek at the top element,i.e.,"""
    return self.top.value
   
  def is_empty(self):
    """method to check if stack is empty return boolean"""
    try:
      if self.top==None:
        return 
    except:
      raise Exception("Stack is empty!!")
     # return self.top
