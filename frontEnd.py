if __name__ == "__main__":
    import os.path
    from os import path
    import keywords
    import parserA
    import testCommands
    from testCommands import SQLBackEnd
    if (path.exists("./server.mdf")):
        os.remove("./server.mdf")
    testCommands.virtualServer = SQLBackEnd('server.mdf')
    print('Please upload Top50SpotifySongs.csv')
    testCommands.virtualServer.uploadCSV('TOP50')
    print('Please upload Top50SpotifyArtists.csv')
    testCommands.virtualServer.uploadCSV('TOP50ARTISTS')
    go = True
    loaded = True
    print("Enter command or type 'help'")
    while go:
        query = input("> ")
        if query == "help":
            print("Available commands: ")
            for word in keywords.KEYWORDS:
                print("  " + word + ": " + keywords.WORD_HELP[word])
            print("  For multi-word entries, delim by \"")
            print("  Multiple commands can be chained together, ie 'popularity of longest song by \"Taylor Swift\"")
        elif query == "quit" or query == "quit()" or query == "q":
            go = False
        else:
            if not loaded:
                print("Need to load .csv file by typing 'load' first.")
            else:
                tree = parserA.parse(query)
                output = tree.evaluate
                print(output)
