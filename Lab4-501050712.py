# Lab4-501050712.py
# Nicolas Metzler
# Student ID: 501050712
# Lab #4 - Huffman Trees
# CPS 305 Section 4J0
# Instructor: J. Tran
# Purpose: To make working Huffman Tree, Encode, Decode, Lookup Table, and Recursive Traverse functions for said Tree.
#
# I hereby attest that I am the sole owner and author of this code (except for skeleton code provided by Prof. Tran) and that to the best of my knowledge, this code has not infringed on anyone’s copyright. Credit for any ideas, coding, and other materials used to develop this code has been given to the owners of the sources used in accordance to the rules of Ryerson's Academic Integrity Policy.

import heapq
import string


def getName():
	return "Metzler, Nicolas"

def orderDict(dictionary, newDict):
    # Start value at the highest number, then find the lowest value in the dictionary
    # Return a new, ordered Dictionary
    value = float('inf')
    dict = dictionary
    for item in dict:
        if dict[item] <= value:
            value = dict[item]
            node = item
    # Recurse if there are more items
    if dict:
        del dict[node]
        newDict.update({node:value})
        orderDict(dict, newDict)
    return newDict

def stringToList(string):
    list = []
    list[:0] = string
    return list

# I don't know how to use heaps yet so I made my own :(
def addToHeap(heap, node):
    index = 0
    returnHeap = heap.copy()
    position = len(heap) - 1
    while position >= 0:
        if heap[position].data > node.data and position - 1 == 0:
            #if at the front of the heap and current node is still more
            returnHeap.insert(position, node)
            break
        elif heap[position].data > node.data and heap[position - 1].data < node.data:
            #if the left is less and right/here is more
            returnHeap.insert(position, node)
            break
        elif heap[position].data < node.data and position + 1 >= len(heap):
            #if at the end of the heap and data is still less
            returnHeap.append(node)
            break
        elif heap[position].data == node.data:
            #if current data is the same
            returnHeap.insert(position, node)
            break
        position -= 1
    return returnHeap

class MyHuffman():
    def __init__(self):
        # Initialize the Huffman tree
        # Dictionary to hold the characters and their coressponding bitcode   
        self.chars = {}
        # Huffman tree
        self.tree = None
        pass

    def build(self, weights):
        # Build a huffman tree from the dictionary of character:value pairs
        leafHeap = []
        # Order the Dictionary in lowest Frequency to greatest Frequency
        freqs = orderDict(weights, {})
        for item in freqs:
            leafNode = Node(item, freqs[item])
            leafHeap.append(leafNode)
        while len(leafHeap) > 1:
            # While heap has more than one node, keep the loop running
            firstNode = leafHeap.pop(0)
            secondNode = leafHeap.pop(0)
            # Create a new parent Node from the two smallest popped Nodes
            if len(leafHeap) == 0:
                    self.tree = Node(None, firstNode.data + secondNode.data, firstNode, secondNode)
            elif firstNode.data < secondNode.data:
                leafHeap = addToHeap(leafHeap.copy(), Node(None, firstNode.data + secondNode.data, firstNode, secondNode))
            elif firstNode.data > secondNode.data:
                leafHeap = addToHeap(leafHeap.copy(), Node(None, firstNode.data + secondNode.data, secondNode, firstNode))
            elif firstNode.data == secondNode.data:
                if firstNode.value is None and secondNode.value is not None:
                    leafHeap = addToHeap(leafHeap.copy(), Node(None, firstNode.data + secondNode.data, secondNode, firstNode))
                else:
                    leafHeap = addToHeap(leafHeap.copy(), Node(None, firstNode.data + secondNode.data, firstNode, secondNode))
        if self.tree is None:
            self.tree = leafHeap[0]
        self.makeLookupTable(self.tree)
        return self.tree
        
    
    def makeLookupTable(self, node, bitCode = None):
        # Recursive algorithm to make a Lookup Table
        if bitCode is None:
            bitCode = []
        if node.value is not None:
            self.chars.update({node.value:bitCode})
            return
        if node.right is not None:
            bitCode.append(0)
            self.makeLookupTable(node.right, bitCode.copy())
        if node.left is not None:
            bitCode[len(bitCode)-1] = 1
            self.makeLookupTable(node.left, bitCode.copy())
        
    def encode(self, word):
        # Return the bitstring of word encoded by the rules of your huffman tree
        charList = stringToList(word)
        bitString = ''
        for item in charList:
            bitCode = self.chars[item]
            for number in bitCode:
                bitString = bitString + str(number)
        return bitString
    
    def decode(self, bitString):
        # Return the word encoded in bitstring, or None if the code is invalid
        node = self.tree
        bitList = stringToList(bitString)
        returnString = ''
        while len(bitList) > 0:
            traverseReturn = self.recursiveTraverseTree(self.tree, bitList.copy())
            returnString = returnString + str(traverseReturn[0])
            bitList = traverseReturn[1]
        return returnString
    
    def recursiveTraverseTree(self, node, bitString):
        # Return the character after traversing the Huffman tree through the bitstring
        #bitList = stringToList(bitString)
        bitList = bitString
        returnString = ''
        if node.value is not None:
            return node.value, bitList
        elif bitList[0] == '1':
            node = node.left
            bitList.pop(0)
            return self.recursiveTraverseTree(node, bitList.copy())
        elif bitList[0] == '0':
            node = node.right
            bitList.pop(0)
            return self.recursiveTraverseTree(node, bitList.copy())


# This node structure might be useful to you
class Node:
    def __init__(self,value,data,left=None,right=None):
        self.left = left
        self.right = right
        self.value = value
        self.data = data

