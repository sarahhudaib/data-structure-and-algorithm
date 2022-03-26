class Node :
  """Like for stacks, we need a node class which will contain the data and a pointer to the next node"""
  def __init__(self,value):
    self.value=value
    self.next=None

class Queue :
  """Next we need the Queue class itself which will contain a 
  constructor initializing the queue and then the methods we require"""
  def __init__(self):
    self.front=None
    self.last=None

  def enqueue(self,value):
    """The enqueue operation will add an element at the end of the queue"""
    node = Node(value)
    if not self.front :
      self.last = node 
      self.front = node 
      
    else:  
      self.last.next = node 
      self.last = node 
      
  def dequeue(self) :
    """Next comes the dequeue operation which removes the front element of the queue"""
    # if self.last == None:
    #   Exception("Queue is empty")
      # return
    if self.last == self.front:
        self.last = None
        self.front = self.front.next
    elif self.last == None:
      Exception("Queue is empty")
    return
    

  def is_empty(self):
    """If the queue is empty, it will print an appropriate message"""
    try:
      if self.last == None:
        return 
    except:
      Exception("Queue is empty")
   

  def peek(self):
    """Now comes the peek method which will return the element at the front of the queue"""
    return self.front.value
