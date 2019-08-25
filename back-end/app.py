#!flask/bin/python
from flask import Flask, jsonify
import projects
import students

app = Flask(__name__)

df_projects = projects._all_projects()
df_students = students._all_students()


def process_dataframe(df):
    result = {}
    for index, row in df.reset_index(drop=True).iterrows():
        result[index] = dict(row)

    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
 

@app.route('/projects/', methods=["GET"])
def all_projects():
    return process_dataframe(df_projects)


@app.route('/students/', methods=["GET"])
def all_students():
    return process_dataframe(df_students)


@app.route('/search/<string:title>', methods=["GET"])
def search(title):
    idx = df_projects["Titulo_do_Projeto"].str.contains(title)
    return process_dataframe(df_projects[idx])


if __name__ == '__main__':
    app.run(debug=True)


