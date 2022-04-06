class StackWithMax:
    def __init__(self):
        self.mainStack = []
        self.trackStack = []

    def push(self, x):
        self.mainStack.append(x)
        if (len(self.mainStack) == 1):
            self.trackStack.append(x)
            return

        # If current element is greater than
        # the top element of track stack,
        # append the current element to track
        # stack otherwise append the element
        # at top of track stack again into it.
        if (x > self.trackStack[-1]):
            self.trackStack.append(x)
        else:
            self.trackStack.append(self.trackStack[-1])

    def getMax(self):
        return self.trackStack[-1]

    def pop(self):
        self.mainStack.pop()
        self.trackStack.pop()


# Driver Code
if __name__ == '__main__':

    s = StackWithMax()
    s.push(20)
    s.push(30)
    s.push(75)
    s.push(10)
    s.push(50)
    print(s.getMax())