from Tree import *

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
    if array[0]:
    newTree = Tree(array[0])
    array.remove[0]
    newTree.setRightChild(buildTree)



