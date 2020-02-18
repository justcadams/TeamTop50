from flask import Flask
from flask import Blueprint, render_template, request
from parser import *
from keywords import *
from backEnd import SQLBackEnd





app = Flask(__name__)
main = Blueprint("main", __name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    errors = []
    data = []
    if request.method == "POST":
        try:
            query = request.form['submission']
            data.append(query)
            go = True
            loaded = False

            if query == "help":
                return render_template("index.html", helpWords=HELP_WORDS_LIST)

            if query =="load":


            return render_template("index.html", Query=data)

        except:
            errors.append("Unable to process your request.")
    return render_template("index.html")






if __name__ == '__main__':

    app.run()


