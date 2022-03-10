class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
                    
class LinkedList():
    def __init__(self):
        self.head = None
        
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
      
    def insert(self, value):
        newNode = Node(value)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
       
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
    ll.append('Sarah')
    ll.append('Ahmad')
    ll.append('Hudaib')
    print(ll)
      
    print (ll.includes('Sarah'))
    print (ll.includes('ZZZZZ'))
    print (ll.includes())


