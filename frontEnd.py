from parser import *

def main():
    rtval = search()
    result = parse(rtval)
    print(result)

def search():
    inp = input("Search: ")
    return inp

main()