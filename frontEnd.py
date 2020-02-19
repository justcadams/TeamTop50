from parserA import *
from keywords import *
from backEnd import SQLBackEnd


if __name__ == "__main__":
    go = True
    loaded = False
    print("Enter command or type 'help'")
    while go:
        query = input("> ")

        if query == "help":
            print("Available commands: ")
            for word in KEYWORDS:
                print("  " + word + ": " + WORD_HELP[word])
            print("  For multi-word entries, delim by \"")
            print("  Multiple commands can be chained together, ie 'popularity of longest song by \"Taylor Swift\"")
        elif query == "load":
            if loaded:
                print("Already loaded csv.")
            else:
                virtualServer = SQLBackEnd('server.mdf')
                virtualServer.uploadCSV()
                loaded = True
        elif query == "quit" or query == "quit()" or query == "q":
            go = False
        else:
            if not loaded:
                print("Need to load .csv file by typing 'load' first.")
            else:
                query = parse(query)
                commandTree = buildTree(query)
                output = commandTree.evaluate()
                print(output)