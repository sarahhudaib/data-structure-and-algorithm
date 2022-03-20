class Node():
    def __init__(self, value=None,next=None):
        self.value = value
        self.next = next
        

                       
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

    def ToString2(msg, head):
        """toString func takes 1 argument so i created this simmiler func to handle both of the linked list"""
        print(msg, end='')
        ptr = head
        while ptr:
            print(ptr.value, end=' —> ')
            ptr = ptr.next
        print('None')
    
    def zip_lists(linked_list_one, linked_list_two):

        if linked_list_one is None:
            return linked_list_two

        if linked_list_two is None:
            return linked_list_one
        
        recur = LinkedList.zip_lists(linked_list_one.next, linked_list_two.next)

        result = linked_list_one      
        linked_list_one.next = linked_list_two       
        linked_list_two.next = recur      

        return result
"""The time complexity of all above-discussed methods is O(m + n),
where m and n are the total number of nodes in the first and second list, respectively."""

"""The recursive solution is the most compact of all 
but is probably not appropriate for production code since it uses stack space 
proportionate to the lists’ lengths."""
 
"""https://stackoverflow.com/questions/58290943/iteratively-recursively-create-a-linked-list """

if __name__ == '__main__':
    linked_list_one = linked_list_two = None
    for i in reversed(range(1, 8, 2)):
        linked_list_one = Node(i, linked_list_one)
 
    for i in reversed(range(2, 8, 2)):
        linked_list_two = Node(i, linked_list_two)

    LinkedList.ToString2('linked_list_one: ', linked_list_one)
    LinkedList.ToString2('linked_list_two: ', linked_list_two)
 
    x = LinkedList.zip_lists(linked_list_one, linked_list_two)
    LinkedList.ToString2('\nAfter Merge: ', x)
            

 
