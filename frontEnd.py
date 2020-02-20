if __name__ == "__main__":
    import os.path
    from os import path
    import keywords
    import parserA
    import commands
    from backEnd import SQLBackEnd
    if (path.exists("./server.mdf")):
        os.remove("./server.mdf")
    commands.virtualServer = SQLBackEnd('server.mdf')
    print('Please upload Top50SpotifySongs.csv')
    commands.virtualServer.uploadCSV('TOP50', './Top50SpotifySongs2019.csv')
    print('Please upload Top50SpotifyArtists.csv')
    commands.virtualServer.uploadCSV('TOP50ARTISTS', './Top50SpotifyArtists2019.csv')
    commands.makeCommandMap(commands.virtualServer)
    
    go = True
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
            tree = parserA.parse(query)
            output = tree.evaluate
            print(output)
                #print("There was an error. Please try again or type 'help'")
