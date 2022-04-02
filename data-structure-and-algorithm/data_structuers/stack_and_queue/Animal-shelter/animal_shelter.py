class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'{self.value}'


class Stack:

    def __init__(self):
        '''initialize stack with top, bottom and length'''
        self.top = None
        self.bottom = None
        self.length = 0

    def isEmpty(self):
        return self.top == None

    def push(self, value):
        '''adds new node to top of stack by pointing it to self.top'''
        node = Node(value)
        node.next = self.top
        self.top = node
        self.length += 1

    def pop(self):
        '''Takes item from top of stack and returns it by reassigning the current top
        to the next item in the stack. Stores the value in a shelter variable to be returned'''
        if self.length <= 0:
            print('nothing to pop')
            return

        shelter = self.top
        self.top = self.top.next
        popped = shelter.value
        self.length -= 1
        return popped

    def peek(self):
        '''prints and returns the top of the stack'''
        if self.length <= 0:
            print('nothing to peek')
            return
        print(self.top.value)
        return self.top.value


class Queue:

    def __init__(self):
        '''initializes a queue instance'''
        self.front = None
        self.rear = None
        self.length = 0

    def isEmpty(self):
        return self.front == None

    def enqueue(self, value):
        '''appends value to front of queue'''

        self.length += 1
        new_node = Node(value)

        if self.rear == None:
            self.front = self.rear = new_node

            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        '''removes value from front of queue, if length is zero it returns the queue
        and prints a message'''
        self.length -= 1

        if self.isEmpty():
            self.queue = []
            print('queue is empty')
            return self.queue

        shelter = self.front
        self.front = shelter.next

        if self.front == None:
            self.rear = None

        return str(shelter.value)

    def peek(self):
        '''returns the first value in a queue'''
        return self.front.value


class Cat():
    def __init__(self):
        self.name = "Cat"


class Dog():
    def __init__(self):
        self.name = "Dog"


class AnimalShelter(Queue):
    """The class AnimalShelter holds only dogs and cats. 
    The shelter operates using a first-in, first-out approach."""
    def __init__(self):

        self.front = None
        self.rear = None
        self.length = 0

    def enqueueDC(self, animal):
        """Adds a new animal to the shelter"""
        if animal == None:
            print('No animal to add !!!! you just wasted your time for nothing!!!')
            return None
        
        elif animal == 'Dog' or animal == 'Cat':
            print(f'We will take care of your {animal}')
            self.enqueue(animal)
            return
        elif animal == 'Dolphin':
            print(f'Seriously a {animal}!!!!!!')
            return None
        # elif animal == None:
        #     print('No animal to add !!!! you just wasted your time for nothing!!!')
        #     return None
        else:
            print('Sorry, we only accept cats and dogs here')
            return None

    def dequeueDC(self, pref=None):
        """ returns either a dog or a cat. If pref is not "dog" or "cat" then return null """

        if pref == None:
            removed = self.dequeue()
            print(
                f'We will help you to choose, what about a little {removed} :3 ')
            return removed

        if pref == "Cat" or pref == 'Dog':
            shelter = self.front

            while (shelter.next is not None and shelter.next.value != pref):
                shelter = shelter.next

            if shelter.next is None:
                print(f'Sorry, there are no available {pref}s right now')
                return None
            else:
                print('shelter', shelter.next)
                removed = shelter.next
                shelter.next = shelter.next.next
                self.length -= 1
                return removed

        else:
            print(f"Sorry, we don't have any {pref}s. Just cats and dogs here")
            return None


if __name__ == '__main__':
    shelter = AnimalShelter()
    shelter.enqueueDC('Dog')
    shelter.enqueueDC('Cat')
    shelter.enqueueDC('Dog')
    shelter.enqueueDC('Cat')
    shelter.enqueueDC('Dog')
    shelter.enqueueDC('Cat')
    shelter.enqueueDC('Dog')
    shelter.enqueueDC('Dog')
    shelter.enqueueDC('Dolphin')
    shelter.enqueueDC('Lion')

    shelter.enqueueDC('Elephant')
    
    # shelter.enqueueDC()

    shelter.dequeueDC("Cat")
    shelter.dequeueDC("Cat")
    shelter.dequeueDC("Cat")
    shelter.dequeueDC()
    shelter.dequeueDC("Dolphin")
