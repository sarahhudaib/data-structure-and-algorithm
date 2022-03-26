class Node():
    def __init__(self, data):
        self.data = data 
        self.next = None 
        self.ptr = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0
        
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            
    def ToString(self):
        if self.head == None:
            print("Empty")
        else:
            current_node = self.head
            while current_node!= None:
                print(current_node.data, end= ' ')
                current_node = current_node.next
        print()
    
    
def reverse_list(linked_list):
    if linked_list.length <=1:
        return linked_list
    else:
        first = linked_list.head
        second = first.next
        linked_list.tail = linked_list.head
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        linked_list.head.next = None
        linked_list.head = first
        return linked_list


def isPalindrome(self, head):
         
        slow_ptr = head
        fast_ptr = head
        prev_of_slow_ptr = head
         
        # To handle odd size list
        midnode = None
         
        # Initialize result
        res = True 
         
        if (head != None and head.next != None):
             
            # Get the middle of the list.
            # Move slow_ptr by 1 and
            # fast_ptr by 2, slow_ptr
            # will have the middle node
            while (fast_ptr != None and
                   fast_ptr.next != None):
                       
                # We need previous of the slow_ptr
                # for linked lists  with odd
                # elements
                fast_ptr = fast_ptr.next.next
                prev_of_slow_ptr = slow_ptr
                slow_ptr = slow_ptr.next
                 
            # fast_ptr would become NULL when
            # there are even elements in the
            # list and not NULL for odd elements.
            # We need to skip the middle node for
            # odd case and store it somewhere so
            # that we can restore the original list
            if (fast_ptr != None):
                midnode = slow_ptr
                slow_ptr = slow_ptr.next
                 
            # Now reverse the second half
            # and compare it with first half
            second_half = slow_ptr
             
            # NULL terminate first half
            prev_of_slow_ptr.next = None
             
            # Reverse the second half
            second_half = self.reverse(second_half)
             
            # Compare
            res = self.compareLists(head, second_half) 
             
            # Construct the original list back
            # Reverse the second half again
            second_half = self.reverse(second_half)
             
            if (midnode != None):
                 
                # If there was a mid node (odd size
                # case) which was not part of either
                # first half or second half.
                prev_of_slow_ptr.next = midnode
                midnode.next = second_half
            else:
                prev_of_slow_ptr.next = second_half
        return res

if __name__ == '__main__':
    my_linked_list = LinkedList()
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)
    my_linked_list.append(5)
    my_linked_list.append(6)
    my_linked_list.ToString()

    reversed_linked_list = reverse_list(my_linked_list)
    reversed_linked_list.ToString()
     
    l = LinkedList()
    s = [ 'a', 'b', 'a', 'c', 'a', 'b', 'a' ]
     
    for i in range(7):
        l.push(s[i])
        l.printList()
         
        if (l.isPalindrome(l.head) != False):
            print("Is Palindrome\n")
        else:
            print("Not Palindrome\n")
        print()
 

        
 

