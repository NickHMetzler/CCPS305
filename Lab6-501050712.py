# Lab6-501050712.py
# Nicolas Metzler
# Student ID: 501050712
# Lab #5 - Hash Tables
# CPS 305 Section 4J0
# Instructor: J. Tran
# Purpose: To make a working Hash Table, Chain Table, and Double Hash Table
#
# I hereby attest that I am the sole owner and author of this code (except for skeleton code provided by Prof. Tran/Liam) and that to the best of my knowledge, this code has not infringed on anyone’s copyright. Credit for any ideas, coding, and other materials used to develop this code has been given to the owners of the sources used in accordance to the rules of Ryerson's Academic Integrity Policy.

def getName():
	return "Metzler, Nicolas"
	
class MyHashTable():
    def __init__(self, size, hash1):
        # Create an empty hashtable with the size given, and stores the function hash1
        self.hashFunction = hash1
        self.array = [None] * size
        self.size = len(self.array) 
        pass
    
    def put(self, key, data):
        # Store data with the key given, return true if successful or false if the data cannot be entered
        if self.isFull() == True:
            return False
        hashKey = self.hashFunction(key)
        if self.array[hashKey] is None:
            self.array[hashKey] = Node(key, data)
            return True
        else:
            return False
        
    def get(self, key):
        # Returns the item linked to the key given, or None if element does not exist
        hashKey = self.hashFunction(key)
        if self.array[hashKey] is None:
            return None
        elif self.array[hashKey].key != key:
            return None
        else:
            return self.array[hashKey].data
        
        
    def __len__(self):
        # Returns the number of items in the Hash Table
        length = 0
        for item in self.array:
            if item is not None:
                length += 1
        return length

    def isFull(self):
        # Returns true if the HashTable cannot accept new members
        for item in self.array:
            if item is None:
                return False
        return True

class MyChainTable(MyHashTable):
    def __init__(self, size, hash1):
        # Create an empty hashtable with the size given, and stores the function hash1
        super().__init__(size,hash1)
        
    
    def put(self, key, data):
        # Store the data with the key given in a list in the table, return true if successful or false if the data cannot be entered
        if self.isFull() == True:
            return False
        hashKey = self.hashFunction(key)
        if self.array[hashKey] is None:
            self.array[hashKey] = Node(key, data)
            return True
        else:
            chosenNode = self.array[hashKey]
            while True:
                if chosenNode.chain is None:
                    chosenNode.chain = Node(key, data)
                    return True
                chosenNode = chosenNode.chain

    def get(self, key):
        # Returns the item linked to the key given, or None if element does not exist
        hashKey = self.hashFunction(key)
        if self.array[hashKey] is None:
            return None
        elif self.array[hashKey].key != key:
            chosenNode = self.array[hashKey]
            while True:
                if chosenNode.key == key:
                    return chosenNode.data
                elif chosenNode.chain is None:
                    return None
                chosenNode = chosenNode.chain
        else:
            return self.array[hashKey].data
        
    def __len__(self):
        # Returns the number of items in the Hash Table
        length = 0
        for item in self.array:
            if item is not None:
                length += 1
                # If a chain exists
                if item.chain is not None:
                    pickedNode = item
                    while True:
                        if pickedNode.chain is not None:
                            length += 1
                            pickedNode = pickedNode.chain
                        else:
                            break
                    
        return length

    def isFull(self):
        # ChainTable will only run out of space when physical memory runs out
        return False

class MyDoubleHashTable(MyHashTable):
    def __init__(self, size, hash1, hash2):
        # Create an empty hashtable with the size given, and stores the functions hash1 and hash2
        super().__init__(size,hash1)
        self.hashFunction2 = hash2
         
    def put(self, key, data):
        # Store data with the key given, return true if successful or false if the data cannot be entered
        if self.isFull() == True:
            return False
        hashKey1 = self.hashFunction(key)
        hashKey2 = self.hashFunction2(key)
        if self.array[hashKey1] is None:
            self.array[hashKey1] = Node(key, data)
            return True
        Key = hashKey1 - hashKey2
        index = 0
        while True:
            # hashKey is out of range
            if Key <= -1:
                Key = self.size + Key
            if self.array[Key] is None:
                self.array[Key] = Node(key, data)
                return True
            # Come full circle
            elif Key == hashKey1:
                return False
            Key = Key - hashKey2
    
    def get(self, key):
        # Returns the item linked to the key given, or None if element does not exist 
        hashKey1 = self.hashFunction(key)
        hashKey2 = self.hashFunction2(key)
        OGKey = hashKey1
        if self.array[hashKey1] is None:
            return None
        elif self.array[hashKey1].key != key:
            hashKey1 = hashKey1 - hashKey2
            chosenNode = self.array[hashKey1]
            while True:
                if hashKey1 <= -1:
                    hashKey1 = self.size + hashKey1
                if chosenNode.key == key:
                    return chosenNode.data
                if hashKey1 == OGKey:
                    return None
                chosenNode = self.array[hashKey1]
                hashKey1 = hashKey1 - hashKey2
        else:
            return self.array[hashKey1].data
        
        
    def __len__(self):
        # Returns the number of items in the Hash Table
        length = 0
        for item in self.array:
            if item is not None:
                length += 1
        return length

class Node:
    def __init__(self, key, data, node=None):
        # Initialize this node, insert data, and set the next node if any
        self.key=key
        self.data=data
        self.chain=node

