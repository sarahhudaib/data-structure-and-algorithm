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
    self.length = 0

  def push(self, value):
    new_node = Node(value)
    if self.top == None: #If the stack is empty, we make the top and bottom pointer both point to the new node
        self.top = new_node
        self.bottom = new_node
    else: #Otherwise, we make the next of the new node, which was pointing to None, point to the present top and then update the top pointer
        new_node.next = self.top
        self.top = new_node
    self.length += 1

  def pop(self):
      if self.top == None: #If the stack is empty, we print an appropriate message
          print("Stack empty")
      else: #Else we make the top pointer point to the next of the top pointer and decrease the length by 1, effectively deleting the top element.
          self.top = self.top.next
          self.length -= 1
          if(self.length == 0): #We make the bottom pointer None if there was only 1 element in the stack and that gets popped
              self.bottom = None

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
