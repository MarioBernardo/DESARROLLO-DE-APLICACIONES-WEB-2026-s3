import json
import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TXT_FILE = os.path.join(BASE_DIR, "data", "servicio.txt")
JSON_FILE = os.path.join(BASE_DIR, "data", "servicio.json")
CSV_FILE = os.path.join(BASE_DIR, "data", "servicio.csv")


def leer_txt():

    datos = []

    with open(TXT_FILE, "r", encoding="utf-8") as f:

        for linea in f:

            datos.append(linea.strip())

    return datos


def leer_json():

    with open(JSON_FILE, "r", encoding="utf-8") as f:

        datos = json.load(f)

    return datos


def leer_csv():

    datos = []

    with open(CSV_FILE, newline="", encoding="utf-8") as f:

        reader = csv.reader(f)

        for fila in reader:

            datos.append(fila)

    return datos