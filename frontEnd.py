from parser import *

def main():
    rtval = search();
    result = parse(rtval)
    print(result)

def search():
    input = input("Search: ")
    return input