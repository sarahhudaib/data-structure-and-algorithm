class Node :
  """Linked Lists are made of nodes. So we create a node class.
     It will contain the data and the pointer to the next node."""
  def __init__(self,value):
    self.value=value
    self.next=None 

class Stack :
  def __init__(self,node=None):
    self.top = node 

  def push(self,value):
    node = Node(value)
    node.next = self.top
    self.top = node 

  def pop(self) :
    try:
      if self.top != None:
        temp = self.top
        self.top = self.top.next
        temp.next= None
      return temp.value
    except:  
      raise Exception("Stack is empty!!")

      

  def peek(self):
    return self.top.value
   
  def is_empty(self):
    """method to check if stack is empty
     return boolean
    """
    try:
      if self.top==None:
        return 
    except:
      raise Exception("Stack is empty!!")
     # return self.top
