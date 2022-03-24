class Stack():
    def __init__(self):
        self.array = []

    def peek(self):
        return self.array[len(self.array)-1]

    def push(self, data):
        self.array.append(data)
        return

    def pop(self):
        if len(self.array)!= 0:
            self.array.pop()
            return
        else:
            print("Stack Empty")
            return



