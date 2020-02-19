from flask import Flask
from flask import Blueprint, render_template, request
from parserA import *
from keywords import *
from backEnd import SQLBackEnd
import testCommands
from testCommands import SQLBackEnd

testCommands.virtualServer = SQLBackEnd('server.mdf')
print('Please upload Top50SpotifySongs.csv')
testCommands.virtualServer.uploadCSV('TOP50')
print('Please upload Top50SpotifyArtists.csv')
testCommands.virtualServer.uploadCSV('TOP50ARTISTS')



app = Flask(__name__)
main = Blueprint("main", __name__)

@app.route('/', methods=['POST', 'GET'])
def index():


    errors = []
    data = []

    if request.method == "POST":
        try:
            queryfromPOST = request.form['submission']
            commandTree = parse(queryfromPOST)
            output = commandTree.evaluate()
            data.append(output)

            go = True
            loaded = True

            if queryfromPOST == "help":

                return render_template("index.html", helpWords=HELP_WORDS_LIST, query=queryfromPOST)

            elif queryfromPOST == "load":
                if loaded:
                    pass
                    return "<h1>Hello world4</h1>"
                else:
                    virtualServer = SQLBackEnd('server.mdf')
                    virtualServer.uploadCSV()
                    loaded = True

            elif not loaded:
                return render_template("index.html", data="CSV needs to be loaded. Type 'Load'", helpWords=HELP_WORDS_LIST, query=queryfromPOST)

            elif go:
                return render_template("index.html", data=data, helpWords=HELP_WORDS_LIST, query=queryfromPOST)

            else:
                return render_template("index.html", data=data, helpWords=HELP_WORDS_LIST, query=queryfromPOST)

        except:
            errors.append("Unable to process your request.")
    return render_template("index.html", helpWords=HELP_WORDS_LIST)






if __name__ == '__main__':

    app.run()


