import pandas as pd
import numpy as np
from HARDCODE import *
from flask import jsonify

DATA_FOLDER = "../data/"
PROJECT_FILE = "projetos.csv"


def _all_projects():
    df = pd.read_csv(DATA_FOLDER+PROJECT_FILE)
    df.drop(columns=["2_Bolsa"], inplace=True)
    situacao_idx = np.random.randint(3, size=len(df))

    df["Situacao_Cor"] = SITUACAO_COLORS[situacao_idx]
    df["Situacao_Desc"] = SITUACAO_DESC[situacao_idx]
    df["Disciplinas"] = DISCIPLINES
    df["Cronograma"] = SCHEDULE
    df["Gastos_Desc"] = FINANCES_DESCRIPTION
    df["Gastos"] = (np.random.randint(3, 10, size=len(df))*100*12).astype(str)
    df["Gastos"] += ",00"
    df["Empresas"] = np.random.choice(EMPRESAS, 1)[0]
    df["Alunos"] = ALUNOS[0] + ', ' + \
                   ALUNOS[1] + ', ' + \
                   ALUNOS[2] + ', ' + \
                   ALUNOS[3] + '\n'

    result = {}

    for index, row in df.iterrows():
        result[index] = dict(row)

    return jsonify(result)