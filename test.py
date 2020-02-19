from flask import Flask
from flask import Blueprint, render_template, request
from parserA import parse
from parserA import buildTree
from keywords import *
from backEnd import SQLBackEnd

s = "popularity of 'Shawn Mendes'"
commandTree = parse(s)
output = commandTree.evaluate()
print(output)






