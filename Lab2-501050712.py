# 2020 Nicolas Metzler, 501050712
# I hereby attest that I am the sole owner and author of this code (except for skeleton code provided by Prof. Tran) and that to the best of my knowledge, this code has not infringed on anyone’s copyright. Credit for any ideas, coding, and other materials used to develop this code has been given to the owners of the sources used in accordance to the rules of Ryerson's Academic Integrity Policy.

def getName():
	return "Metzler, Nicolas"

class MyQueue:
    def __init__(self, data=None, maxSize = 100000):
        # Initialize this queue, variables are to log the location of the front, tail, size, and queue itself
        self.front = 0
        self.tail = 0
        self.size = 0
        # self.maxSize variable is helpful to replace len(self.items) in comparisons
        self.maxSize = maxSize
        self.items = [None] * maxSize
        # If data exists, add it to the queue
        if data != None:
            self.enqueue(data)

    # Add data to the end of the queue, make it circular
    def enqueue(self, data):
        # Check if tail points to head (queue full)
        if (self.tail == self.front and self.items[self.front] != None) or (self.tail >= self.maxSize and self.front <= 0):
            return
        # Check if tail exceeds boundaries
        elif self.tail >= self.maxSize:
            self.tail = 0
        # Add data to queue, and adjust variables
        self.items[self.tail] = data
        self.tail += 1            
        self.size += 1
    
    # Return the data at the beginning of the queue, or None if the queue is empty
    def dequeue(self):
        # Check if the queue exists
        if self.size <= 0:
            return None
        # Check if the front exceeds boundaries, adjust variables as required
        elif self.front >= self.maxSize:
            self.front = 0
            dequeuedElement = self.items[self.front]
        else:
            dequeuedElement = self.items[self.front]
            self.front += 1
        self.size -= 1
        return dequeuedElement

    def __len__(self):
        # Return the number of elements in the queue
        return self.size

class MyStack:
    def __init__(self, data=None, maxSize = 100000):
        # Initialize this stack and the size
        self.size = 0
        # self.maxSize variable is helpful to replace len(self.items) in comparisons
        self.maxSize = maxSize
        self.items = [None] * maxSize
        # If data exists, add it to the stack
        if data != None:
            self.push(data)
    
    # Add data to the top of the stack
    def push(self, data):
        # Check if stack is full
        if self.size < self.maxSize:
            # Add data to stack, and adjust size
            self.items[self.size] = data
            self.size += 1

    # Return the data at the top of the stack, or None if the stack is empty
    def pop(self):
        # Check if the stack exists
        if self.size > 0:
            # Return popped element, and adjust size
            self.size -= 1
            return self.items[self.size]

    def __len__(self):
        # Return the number of elements in the stack
        return self.size

    def peek(self):
        # Return item under the top of the stack if it exists
        if self.size > 1:
            return self.items[self.size - 2]