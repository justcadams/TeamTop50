from parser import *

if __name__ == "__main__":
    go = True
    print("Enter command or type 'help'.")
    while go:
        query = input("Input: ")

        if query == "help":
            print("TYPE SOMETHING")
        elif query == "quit":
            go = False
        else:
            # TODO
            # Execute command or throw error
            print("TODO")
