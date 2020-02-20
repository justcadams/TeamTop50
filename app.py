
import parserA as parserA
from keywords import *
import commands
from commands import SQLBackEnd
from flask import Flask
from flask import render_template, request



global app
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    errors = []
    data = []
    runaround = 0



    if runaround == 0:
        # if (os.path.exists("./server.mdf")):
        #     os.remove("./server.mdf")
        commands.virtualServer = SQLBackEnd('server.mdf')
        print('Please upload Top50SpotifySongs.csv')
        commands.virtualServer.uploadCSV('TOP50', './Top50SpotifySongs2019.csv')
        print('Please upload Top50SpotifyArtists.csv')
        commands.virtualServer.uploadCSV('TOP50ARTISTS', './Top50SpotifyArtists2019.csv')
        runaround += 1

    if request.method == "POST":

        queryfromPOST = request.form['submission']
        errors.append(queryfromPOST)
        errors.append(type(queryfromPOST))
        tree = parserA.parse(queryfromPOST)
        errors.append(str(tree))
        errors.append(type(tree))

        information = tree.evaluate

        if isinstance(information, int):
            data.append(information)
        if isinstance(information, str):
            data.append(information.split(',')[0])
        if isinstance(information, list):
            data.append(information[0])
        if isinstance(information, float):
            data.append(information)

        try:
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
            return render_template("index.html", helpWords=HELP_WORDS_LIST, query=errors)
    return render_template("index.html", helpWords=HELP_WORDS_LIST)


if __name__ == '__main__':

    app.run()


