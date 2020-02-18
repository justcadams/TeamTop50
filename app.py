from flask import Flask
from flask import Blueprint, render_template, request





app = Flask(__name__)
main = Blueprint("main", __name__)

@app.route('/', methods=['PUT'])
def index():

    data = [['text', "First"], ['text', "Second"], ['text', "Third"]]
    return render_template("index.html", data=data)


@app.route('/', methods=["PUT"])
def submission():

    data = []
    return render_template("index.html", data=data)



if __name__ == '__main__':

    app.run()


