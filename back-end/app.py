#!flask/bin/python
from flask import Flask
import projects

app = Flask(__name__)

@app.route('/projects/', methods=["GET"])
def all_projects():
    return projects._all_projects()

if __name__ == '__main__':
    app.run(debug=True)


