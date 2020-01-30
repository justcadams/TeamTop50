def parse(search):
    search_array = []
    for c in search:
        word = ""
        if c == " ":
            search_array.append(word)
            word = ""
        else:
            word += c