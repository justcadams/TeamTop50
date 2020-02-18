import shlex
from Tree import *
from keywords import *


# parse function takes the search query and places words and phrases into an array
# buzzwords are removed and keywords preserved (see keywords.py)
# this array is passed to buildTree and a tree is returned
def parse(query):
    # Splits query into array, preserving words in quotation marks
    words = shlex.split(query)
    for BUZZWORD in BUZZWORDS:
        words = [word for word in words if word != BUZZWORD]

    # Finds keywords that are longer than one word and combines them
    N = len(words)
    i = 0
    while i < len(words) - 1:
        tmp = words[i] + " " + words[i + 1]
        if tmp in KEYWORDS:
            words[i] = tmp
            del (words[i + 1])
        i = i + 1
    # call buildTree
    searchTree = buildTree(words)
    return searchTree


# buildTree function takes in the array from the parse function and places each array element into the tree structure
# defined in Tree.py and returns a tree object
def buildTree(array):
    # Base case is when input array has length 1
    if len(array) == 1:
        return Tree(array[0])
    # check if first item in array is unary keyword
    elif array[0] not in BINARY_KEYWORDS:
        newTree = Tree(array[0])
        array.pop(0)
        newTree.setRightChild(buildTree(array))
        return newTree

    # run else if binary keyword detected as first element in array
    else:
        newTree = Tree(array[0])
        array.pop(0)
        # call split index function
        index = splitIndex(array, "and")
        # if error, set child to -1 and return tree
        if index == -1:
            newTree.setRightChild(-1)
            return newTree
        # if no error, place all elements on the left of the delim as left child and all elements to the right in right child
        # eliminate the delim character, and return tree.
        else:
            newTree.setLeftChild(buildTree(array[0:index]))
            newTree.setRightChild(buildTree(array[index+1:]))
            return newTree


def splitIndex(array, delim):
    count = 0   # count variable used to keep track of encapsulated binary arguments
    index = 0  # index for the split point

    # loop through to find index of delimiter
    while (array[index] != delim) or (count != 0):
        # keep tally of all Binary Keywords and delims to allow for multiple binary arguments
        if array[index] in BINARY_KEYWORDS:
            count += 1
        elif array[index] == delim:
            count -= 1
        index += 1
        # if index goes out of range, return error -1
        if index == len(array):
            return -1
    return index
