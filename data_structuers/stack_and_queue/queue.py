class Node :
  def __init__(self,value):
    self.value=value
    self.next=None


class Queue :
  def __init__(self):
    self.front=None
    self.last=None

  def enqueue(self,value):
    node = Node(value)
    
    if not self.front :
      self.last = node 
      self.front = node 
      
    else:  
      self.last.next = node 
      self.last = node 
      
  def dequeue(self) :
    if self.last == self.first:
      self.last = None
    self.first = self.first.next
    return
    

  def is_empty(self):
    if self.last == None:
      print("Queue Empty")

  def peek(self):
    return self.first.value
