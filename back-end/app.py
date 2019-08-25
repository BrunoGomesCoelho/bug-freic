#!flask/bin/python
from flask import Flask
import projects
import students

app = Flask(__name__)

@app.route('/projects/', methods=["GET"])
def all_projects():
    response = projects._all_projects()
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/students/', methods=["GET"])
def all_students():
    response = students._all_students()
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True)


