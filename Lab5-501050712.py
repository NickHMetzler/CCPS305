# Lab5-501050712.py
# Nicolas Metzler
# Student ID: 501050712
# Lab #5 - Tries
# CPS 305 Section 4J0
# Instructor: J. Tran
# Purpose: To make working Trie Tree, Insert, Length, Exists and AutoComplete functions for said Tree.
#
# I hereby attest that I am the sole owner and author of this code (except for skeleton code provided by Prof. Tran/Liam) and that to the best of my knowledge, this code has not infringed on anyone’s copyright. Credit for any ideas, coding, and other materials used to develop this code has been given to the owners of the sources used in accordance to the rules of Ryerson's Academic Integrity Policy.

def getName():
	return "Metzler, Nicolas"

class MyTrie:
    def __init__(self, word = None):
        # Initialize the trie node
        self.checklist = []
        self.autocomplete_list = []
        self.children = {}
        self.children_count = 0
        self.string = word
    
    def insert(self, word):
        # Check if word is already in Tree
        for item in self.checklist:
            if item == word:
                # Word already exists in Trie
                return
        # Insert word and add it to the checklist
        self.recursiveInsert(word)
        self.checklist.append(word)
    
    def recursiveInsert(self, word, index = 0):
        # Insert word by recursively making nodes or moving through existing nodes
        if index <= len(word) - 1:
            letter = word[index]
            if letter in self.children:
                # There is already a node for this letter
                pass
            else:
                # Create a node for this letter and sort the children
                self.children[letter] = MyTrie()
                sortingList = list(self.children.items())
                sortingList.sort()
                self.children = dict(sortingList)
            if index == len(word) - 1:
                # Reached the end of the word, add it to the Trie
                self.children[letter].children['#'] = MyTrie(word)
                return
            # Recursively add the letters until a base case is reached
            self.children[letter].recursiveInsert(word, index + 1)
            
    def exists(self, word, position=0):
        # Return true if the passed word exists in this trie node
        if position <= len(word) - 1 and word[position] in self.children:
            # Recurse until we reach the end of the word
            return self.children[word[position]].exists(word, position + 1)
        elif word == '' and self.isTerminal() == True:
            # A terminal node will return true if the word passed is ""
            return True
        if '#' in self.children:
            # Check if this is a terminal node
            if self.children['#'].string == word:
                # Word was found
                return True
            else:
                return False
        else:
            return False
        
        
    def isTerminal(self):
        # Return true if this node is the terminal point of a word
        if self.string is not None:
            return True
        return False

    def autoComplete(self, prefix, position = 0):
        # Reset autocomplete_list variable
        self.autocomplete_list = []
        # Get all the matches and return the list
        self.recursiveAutoComplete(self, prefix, position)
        return self.autocomplete_list

    def recursiveAutoComplete(self, node, prefix = '', position=0):
        # Return every word that extends this prefix in alphabetical order
        if position <= len(prefix) - 1 and prefix[position] in node.children:
            # Repeat until we've found the starting node to search
            return self.recursiveAutoComplete(node.children[prefix[position]], prefix, position + 1)
        elif position <= len(prefix) - 1 and prefix[position] not in node.children:
            # No such word exists
            return []
        if '#' in node.children and len(node.children) <= 1:
            # Terminal node
            self.autocomplete_list.append(node.children['#'].string)
        elif '#' in node.children and len(node.children) >= 2:
            # Terminal node, and more children tries to search
            self.autocomplete_list.append(node.children['#'].string)
            for element in node.children:
                self.recursiveAutoComplete(node.children[element], prefix, position)
        elif len(node.children) >= 1:
            # Search all children Tries for more words
            for element in node.children:
                self.recursiveAutoComplete(node.children[element], prefix, position)
            
    def __len__(self):
        returnLen = 0
        # Recursively get the length
        if '#' in self.children and len(self.children) <= 1:
            # Terminal node
            return 1
        elif '#' in self.children and len(self.children) >= 2:
            # terminal node, and more children to search
            returnLen += 1
            for node in self.children:
                returnLen += self.children[node].__len__()
        elif len(self.children) >= 1:
            # Search all children tries
            for node in self.children:
                returnLen += self.children[node].__len__()
        # Return the length
        return returnLen
        

