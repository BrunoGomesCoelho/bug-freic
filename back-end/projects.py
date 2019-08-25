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
    df["Empresas"] = EMPRESAS[np.random.randint(len(EMPRESAS), size=len(df))]
    df["Alunos"] = ALUNOS[0] + ', ' + \
                   ALUNOS[1] + ', ' + \
                   ALUNOS[2] + ', ' + \
                   ALUNOS[3] + '\n'

    # Get dates
    df["Data_inicio"] = pd.date_range(start='01/01/2019', end='24/08/2019', \
                                      periods=len(df))
    df["Data_fim"] = pd.date_range(start='25/10/2019', end='01/01/2021', \
                                      periods=len(df))
    # Correctly get format day-month-year
    for col in ["Data_inicio", "Data_fim"]:
        temp = df[col].copy(deep=True)
        df[col] = temp.dt.day.astype(str) + "-"
        df[col] += temp.dt.month.astype(str) + "-" 
        df[col] += temp.dt.year.astype(str)

    result = {}

    for index, row in df.iterrows():
        result[index] = dict(row)

    return jsonify(result)
