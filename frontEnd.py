from parser import *

if __name__ == "__main__":
    go = True
    print("Enter command or type 'help'")
    while go:
        query = input("> ")

        if query == "help":
            print("TYPE SOMETHING")
        elif query == "quit" or query == "quit()":
            go = False
        else:
            # TODO
            # Execute command or throw error
            query = parse(query)
            commandTree = buildTree(query)
            output = commandTree.evaluate()
            print(output)


