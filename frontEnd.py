from parser import *

if __name__ == "__main__":
    go = True
    print("Enter command or type 'help'")
    while go:
        query = input("> ")

        if query == "help":
            print("TYPE SOMETHING")
        elif query == "quit":
            go = False
        else:
            # TODO
            # Execute command or throw error
            valid = True


            if valid:
                print("TODO")
                print("TODO: output here")
            else:
                print("Invalid command. Try again or type 'help'")

