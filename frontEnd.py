from parser import *
from keywords import *
from backEnd import SQLBackEnd


if __name__ == "__main__":
    go = True
    loaded = False
    tree = parse()
    print("Enter command or type 'help'")
    virtualServer = SQLBackEnd('Top50.mdf')
    while go:
        query = input("> ")
        if query == "help":
            print("Available commands: ")
            for word in KEYWORDS:
                print("  " + word + ": " + WORD_HELP[word])
            print("  For multi-word entries, delim by \"")
            print("  Multiple commands can be chained together, ie 'popularity of longest song by \"Taylor Swift\"")
        elif query == "quit" or query == "quit()" or query == "q":
            go = False
        else:
            if not loaded:
                print("Need to load .csv file by typing 'load' first.")
            else:
                tree = parse(query)
                output = tree.evaluate()
                print(output)