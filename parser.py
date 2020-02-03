from Tree import *

BINARY_KEYWORDS = ["compare", "more"]
def parse(search):
    array = []
    for c in search:
        word = ""
        if c == " ":
            if word in ["of","by"]:
                word = ""
            else:
                array.append(word)
                word = ""
        else:
            word += c
    return array

def buildTree(array):
    if array[0] != BINARY_KEYWORDS:
        Tree newTree = Tree(array[0])
        array.remove[0]
        newTree.setRightChild(buildTree(array))
    elif array[0] == ["compare"]
        Tree newTree = Tree(array[0]+array[1])
        array.remove[0]
        array.remove[1]
        count = 0
        index = 0
        while (array[index] != "and") and (count != 0):
            if array[index] == BINARY_KEYWORDS:
                count ++
            if array


