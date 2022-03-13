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
                
if __name__=="__main__":
    pass
    ll = LinkedList()
    sarah = Node("Sarah")
    ahmad = Node("Ahmad")
    Hudaib = Node("Hudaib")
    ll.append(sarah)
    ll.insert(ahmad)
    ll.insert(Hudaib)
    print(ll)
      
    # print (ll.includes('Sarah'))
    # print (ll.includes('ZZZZZ'))
    print(ll.insert_after("Ahmad", 10001))    
    print(ll.insert_before("Sarah", 10002))
    print(ll)
