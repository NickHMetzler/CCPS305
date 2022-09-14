# Lab3-501050712.py
# Nicolas Metzler
# Student ID: 501050712
# Assignment #2 - Simulate Pop Machine
# CPS 305 Section 4J0
# Instructor: J. Tran
# Purpose: To make working Complete Tree, Binary Search Tree, and AVL Tree classes.
#
# I hereby attest that I am the sole owner and author of this code (except for skeleton code provided by Prof. Tran) and that to the best of my knowledge, this code has not infringed on anyone’s copyright. Credit for any ideas, coding, and other materials used to develop this code has been given to the owners of the sources used in accordance to the rules of Ryerson's Academic Integrity Policy.

def getName():
	return "Metzler, Nicolas"

# Function to return the greater of 2 values, used in getHeight()
def getMax(value1, value2):
    if value1 >= value2:
        return value1
    else:
        return value2
	
class MyTree():
    def __init__(self, data):
        # Initialize this Node, and store data in it
        self.data = data
        self.left = None
        self.right = None
        self.height = 0
        self.descendants = 0
    
    def getLeft(self):
        # Return the left child of this Node, or None
        return self.left
    
    def getRight(self):
        # Return the right child of this Node, or None
        return self.right
    
    def getData(self):
        # Return the data contained in this Node
        return self.data
    
    def maxDescendants(self):
        # Find the maximum amount of Descendents
        # Recursively calculate the summation of 2^n, n = self.height, i = 1
        maximum = 0
        countdown = self.height
        while countdown >= 1:
            maximum = maximum + (2**countdown)
            countdown -= 1
        return maximum
    
    def insert(self, data):
        # Insert data into the tree, descending from this Node
        # Check if left is None first, then if right is None
        if self.left is None:
            self.left = MyTree(data)
        elif self.right is None:
            self.right = MyTree(data)
        # Check the descendants to find where to recurse
        else:
            if self.left.descendants == self.right.descendants or (self.left.height == self.right.height + 1 and self.left.descendants < self.left.maxDescendants()):
                self.left.insert(data)
            else:
                self.right.insert(data)
        # Update the height and descendants and return self
        self.getDescendants()
        self.getHeight()
        return self
        
    def getDescendants(self):
        # Update all descendants from the calling Node, downwards due to recursion
        # If both exist, add the descendants and add 2
        if self.left is not None and self.right is not None:
            self.descendants = self.left.getDescendants() + self.right.getDescendants() + 2
        # If one child exists take the descendants and add 1
        elif self.right is None and self.left is not None:
            self.descendants = self.left.getDescendants() + 1
        elif self.left is None and self.right is not None:
            self.descendants = self.right.getDescendants() + 1  
        # No Children means it's a leaf Node
        else:
            self.descendants = 0
        return self.descendants

    def getHeight(self):
        # Update all heights from the calling Node, downwards due to recursion
        # If both exist, find the max and add 1
        if self.left is not None and self.right is not None:
            self.height = getMax(self.left.getHeight(), self.right.getHeight()) + 1
        # If one child exists take it and add 1
        elif self.left is not None and self.right is None:
            self.height = self.left.getHeight() + 1
        elif self.right is not None and self.left is None:
            self.height = self.right.getHeight() + 1
        # No Children means it's a leaf Node
        else:
            self.height = 0
        return self.height

class MyBST(MyTree):
    def __init__(self, data):
        # Initialize this Node, and store data in it
        super().__init__(data)
        pass

    def insert(self, data):
        # Insert data into the tree, descending from this Node
        # Ensure that the tree remains a valid Binary Search Tree
        if data < self.data:
            # Data belongs to the left
            if self.left is None:
                self.left = MyBST(data)
            else:
                self.left.insert(data)
        elif data >= self.data:
            # Data belongs to the right or is already in Tree
            if self.right is None:
                self.right = MyBST(data)
            else:
                self.right.insert(data)
        # Update the height and return self
        self.getHeight()
        return self

    def __contains__(self, data):
        # Returns True if data is in this Node or a child of it, returns false if it does not exist
        if data == self.data:
            return True
        elif data < self.data and self.left is not None:
            return self.left.__contains__(data)
        elif data > self.data and self.right is not None:
            return self.right.__contains__(data)
        else:
            return False
        

class MyAVL(MyBST):
    def __init__(self, data):
        # Initialize this Node, and store data in it
        super().__init__(data)
        pass

    def getBalanceFactor(self):
        # Return the balance factor of this Node
        if self.left is None and self.right is None:
            return 0
        elif self.left is None:
            return ((-1) - self.right.height)
        elif self.right is None:
            return (self.left.height + 1)
        else:
            return (self.left.height - self.right.height)
        
    def insert(self, data):
        # Insert data into the tree, descending from this Node
        # Ensure that the tree remains a valid AVL tree
        if data < self.data:
            # Data belongs to the left
            if self.left == None:
                # If child is empty
                self.left = MyAVL(data)
            else:
                # Recursion if empty space is not found
                self.left = self.left.insert(data)
        elif data > self.data or data == self.data:
            # Data belongs to the right or is already in Tree
            if self.right == None:
                # If child is empty
                self.right = MyAVL(data)                
            else:
                # Recursion if empty space is not found
                self.right = self.right.insert(data)
        # Check for rotations and perform them if needed        
        newValue = self
        selfBalance = self.getBalanceFactor()
        if self.left is not None:
            leftBalance = self.left.getBalanceFactor()
        else:
            leftBalance = 0
        if self.right is not None:
            rightBalance = self.right.getBalanceFactor()
        else:
            rightBalance = 0
        
        if selfBalance >= 2 and leftBalance >= 1:
            newValue = self.rightRotate()
        elif selfBalance <= -2 and rightBalance <= -1:
            newValue = self.leftRotate()
        elif selfBalance >= 2 and leftBalance <= -1: 
            self.left = self.left.leftRotate()
            newValue = self.rightRotate()
        elif selfBalance <= -2 and rightBalance >= 1:
            self.right = self.right.rightRotate()
            newValue = self.leftRotate()
        # Update the height and return newValue (self if no rotations)
        newValue.getHeight()    
        return newValue


    def leftRotate(self):
        # Set temp variables/pointers
        newTop = self.right
        shiftedChildren = newTop.left

        # Perform rotation
        newTop.left = self
        self.right = shiftedChildren

        return newTop

    def rightRotate(self):
        # Set temp variables/pointers
        newTop = self.left
        shiftedChildren = newTop.right

        # Perform rotation
        newTop.right = self
        self.left = shiftedChildren

        return newTop
