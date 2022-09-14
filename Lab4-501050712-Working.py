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
        self.chars = {}
        #dictionary to hold the characters and their coressponding bitcode
        
        #Huffman tree
        self.tree = None
        # position in the bitstring being decoded
        self.decodePosition = 0
        pass

    def build(self, weights):
        # Build a huffman tree from the dictionary of character:value pairs
        leafHeap = []
        # Order the Dictionary in lowest Frequency to greatest Frequency
        freqs = orderDict(weights, {})
        for item in freqs:
            leafNode = Node(item,freqs[item])
            leafHeap.append(leafNode)
        while len(leafHeap) > 1:
            # While heap has more than one node, keep the loop running
            firstNode = leafHeap.pop(0)
            secondNode = leafHeap.pop(0)
            # Create a new parent Node from the two chosen Nodes
            if len(leafHeap) == 0:
                    self.tree = Node(None, firstNode.data + secondNode.data, firstNode, secondNode)
            elif firstNode.data < secondNode.data:
                leafHeap = addToHeap(leafHeap.copy(), Node(None, firstNode.data + secondNode.data, firstNode, secondNode))
            elif firstNode.data > secondNode.data:
                leafHeap = addToHeap(leafHeap.copy(), Node(None, firstNode.data + secondNode.data, secondNode, firstNode))
            elif firstNode.data == secondNode.data:
                if firstNode.value is None and secondNode.value is not None:
                    leafHeap = addToHeap(leafHeap.copy(), Node(None, firstNode.data + secondNode.data, secondNode, firstNode))
                elif firstNode.value is not None and secondNode.value is None:
                    leafHeap = addToHeap(leafHeap.copy(), Node(None, firstNode.data + secondNode.data, firstNode, secondNode))
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
        while len(bitList) != 0:
            if bitList[0] == '1':
                node = node.left
            elif bitList[0] == '0':
                node = node.right
            else:
                return None
            bitList.pop(0)
            if node.value is not None:
                # If a value is found, start searching for the next value
                returnString = returnString + str(node.value)
                node = self.tree
        return returnString
    
    def recursiveTraverseTree(self, node, bitString):
        # Return the character after traversing the Huffman tree through the bitstring
        bitList = stringToList(bitString)
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

