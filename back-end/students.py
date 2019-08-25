#!flask/bin/python
import pandas as pd
from flask import Flask, jsonify
from HARDCODE import *

DATA_FOLDER = "../data/"
PROJECT_FILE = "projetos.csv" 
TESTING = False

def _all_students():
    temp = pd.read_csv(DATA_FOLDER+PROJECT_FILE)
    size = len(temp)

    cols = ["NUSP", "Nome", "Media", "Semestre", "Creditos_Acumulados"]
    df = pd.DataFrame(columns=cols)

    df["Nome"] = temp["Nome_do_Pesquisador"]
    df["NUSP"] = np.random.randint(8000000, 9999999, size=size)
    df["Media"] = np.random.normal(7.0, 2.1, size=size)
    df["Semestre"] = np.random.randint(1, 8, size=size)
    df["Creditos_Acumulados"] = np.random.randint(12, 156, size=size)

    for col in cols:
        df[col] = df[col].astype(str)
    df["Media"] = df["Media"].apply(lambda x: x[:4])

    if TESTING:
        df.to_csv("students.csv", index=False)
    return df

