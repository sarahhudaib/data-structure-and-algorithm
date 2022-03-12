class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
                    
class LinkedList():
    def __init__(self):
        self.head = None
   
    def ToString(self):
        return self.__str__()
        
    def append(self,values):
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
    

if __name__=="__main__":
    ll = LinkedList()
    sarah = Node("Sarah")
    ahmad = Node("Ahmad")
    Hudaib = Node("Hudaib")
    ll.append(sarah)
    ll.insert(ahmad)
    ll.append(Hudaib)
    print(ll)
      
    print (ll.includes('Sarah'))
    print (ll.includes('ZZZZZ'))
    # print (ll.includes())


