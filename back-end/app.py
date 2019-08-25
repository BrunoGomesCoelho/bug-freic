#!flask/bin/python
from flask import Flask, jsonify
import projects
import students

app = Flask(__name__)

df_projects = projects._all_projects()
df_students = students._all_students()

@app.route('/projects/', methods=["GET"])
def all_projects():
    result = {}
    for index, row in df_projects.iterrows():
        result[index] = dict(row)

    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/students/', methods=["GET"])
def all_students():
    result = {}
    for index, row in df_students.iterrows():
        result[index] = dict(row)

    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/search/<string:hi>', methods=["GET"])
def search(hi):
    print(hi)
    return None


if __name__ == '__main__':
    app.run(debug=True)


