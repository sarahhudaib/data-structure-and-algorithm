class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'{self.value}'


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def isEmpty(self):
        return self.top == None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self.length += 1

    def pop(self):
        if self.length <= 0:
            print('Stack is empty')
            return
        temp = self.top
        self.top = self.top.next
        popped = temp.value
        self.length -= 1
        return popped

    def peek(self):
        if self.length <= 0:
            print('Stack is empty')
            return
        print(self.top.value)
        return self.top.value


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
        
    def isEmpty(self):
        return self.front == None

    def enqueue(self, value):
        self.length += 1
        new_node = Node(value)
        if self.rear == None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        self.length -= 1
        if self.isEmpty():
            self.queue = []
            print('queue is empty')
            return self.queue
        temp = self.front
        self.front = temp.next
        if self.front == None:
            self.rear = None
        return str(temp.value)

    def peek(self):
        return self.front.value
#-----------------------------------------Pseudo Queue-------------------------------------------------------------
class PseudoQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, value):
        ''' Push the value to be added onto the stack Then rebuild the main stack by iterating over the helper stack
        and pushing each node onto the main stack'''

        while self.s1.length != 0:
            current = self.s1.pop()
            self.s2.push(current)

        self.s2.push(value)

        while self.s2.length != 0:
            current = self.s2.pop()
            self.s1.push(current)

    def dequeue(self):
        if self.s1.top:
            return self.s1.pop()

        return None
