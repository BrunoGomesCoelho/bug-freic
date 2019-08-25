#!flask/bin/python
from flask import Flask
import projects
import students

app = Flask(__name__)

@app.route('/projects/', methods=["GET"])
def all_projects():
    return projects._all_projects()

@app.route('/students/', methods=["GET"])
def all_students():
    return students._all_students()

if __name__ == '__main__':
    app.run(debug=True)


