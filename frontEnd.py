from parser import *

def main():
    rtval = search();
    result = parse(rtval)
    print(result)

def search():
    input = raw_input("Search: ")
    return input