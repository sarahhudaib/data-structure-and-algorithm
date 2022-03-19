class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
                    
class LinkedList():
    def __init__(self):
        self.head = None
   
    def ToString(self):
        return self.__str__()
    
    def __str__(self):
        values = '  Head-->  '
        if self.head is None:
            values = 'This Linked List is empty'
        else:
            current = self.head
            while (current):
                values += f'{current.value}->  '
                current = current.next
            values+="None"
        return values
        
      
    def insert(self, new_node):
        if new_node == '':
            raise TypeError('Node must not be empty')
        else:
            new_node.next = self.head
            self.head = new_node
       
    def includes(self, value):
        if value is None:
            raise  TypeError('MISSING ARGUMENT VALUE!!') 
        else:
            current = self.head
            while current:
                if current.value == value:
                    return True
                current = current.next
            print (value)
            return False
    
    def append(self,values):
        ''' takes in a value and adds it to the end of the list '''
        if values == '':
            raise TypeError('Node must not be empty')
        else:            
            if self.head is None:
                self.head = values
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = values
                    
    def insert_before(self, value, new_val):
            ''' method that takes 2 arguments value and new value & adds a new node 
with the given new value immediately before the first node that has the value specified'''
            node = Node(new_val)
            current = self.head
            while current:
                if current.value == value:
                    node.next = current
                    self.head = node
                    return
                if current.next:
                    if current.next.value == value:
                        node.next = current.next
                        current.next = node
                        return
                    current = current.next
            raise ValueError(f'{value} not found')
        
    def insert_after(self, value, new_value):
        '''method that takes 2 arguments value and new value and arguments: 
value, new value adds a new node with the given new value immediately after 
the first node that has the value specified'''
        node = Node(new_value)
        current = self.head
        while current:
            if current.value == value:
                node.next = current.next
                current.next = node
                return
            current = current.next
        raise ValueError(f'{value} not found')
   
    def length_(self):
        """length method will help to determine the length of 
        the list to use it in the kth_form_end() func """
        length = 0
        current = self.head
        while current:
            length+=1
            current = current.next
        return length
    
    def kth_from_end(self, k):
        """kth from end
        argument: a number, k, as a parameter.
        Return the nodes value that is k places from the tail of the linked list """
        
        length = self.length_()
        if not -length <= k < length:
            return ("k not in the range")
        next_node = None
        if k >= 0:
            next_node = length -k -1
        if k < 0:
            next_node = k-1
        current = self.head
        #"we don't care about the iterator value, just that it should run some specific number of times"
        for _ in range(next_node):
            """When you are not interested in some values returned by a function we use underscore in place 
            of variable name . Basically it means you are not interested in how many times the loop 
            is run till now just that it should run some specific number of times overall."""
            current = current.next
        return current.value

