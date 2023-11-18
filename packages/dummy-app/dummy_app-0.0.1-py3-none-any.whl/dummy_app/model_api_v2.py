import flask
from flask import request, jsonify

# from sqlalchemy import null

# model packages
from random import randint
import pandas as pd

# import sklearn as skl
from sklearn.linear_model import LinearRegression
import pickle
import sqlite3
import os
import datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def getTime():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time


# Pathing
path = ""
# path = "02_python_apps/API testing/"
db_file = path + "test.db"
model_file = path + "finalized_model.sav"


# Clear and generate database
def generate_database(data_sets):
    if os.path.exists(db_file):
        os.remove(db_file)
    conn = sqlite3.connect(db_file)
    # cursor = conn.cursor()
    # queries = [
    #     """
    #     CREATE TABLE {table_name}_DATA (
    #     c1 int,
    #     c2 int,
    #     c3 int
    #     )
    #     """.format(table_name = x)
    #     for x in data_sets
    # ]
    # print(queries)
    # [cursor.execute(x) for x in queries]

    # Query data from the table
    select_query = "SELECT * FROM sqlite_master;"
    # res = cursor.execute(select_query).fetchall()
    res = pd.read_sql_query(select_query, conn)
    return {"output": res}


# Help data generation function
def generate_sample_data():
    sample_data = list()
    TRAIN_SET_LIMIT = 1000
    TRAIN_SET_COUNT = 100
    for i in range(TRAIN_SET_COUNT):
        a = randint(0, TRAIN_SET_LIMIT)
        b = randint(0, TRAIN_SET_LIMIT)
        c = randint(0, TRAIN_SET_LIMIT)
        op = a + (2 * b) + (3 * c) + randint(-100, 100)
        sample_data.append([a, b, c, op])
    output = pd.DataFrame(sample_data)
    return output


# Creates and loads data into database
def generate_data(data_sets):
    conn = sqlite3.connect(db_file)
    output_dict = {}
    for data_set in data_sets:
        data = generate_sample_data()
        data.to_sql(data_set, conn, if_exists="replace")
        output_dict[data_set] = data.to_dict()
    return output_dict


@app.route("/", methods=["GET"])
def home():
    return jsonify(message="hello")


@app.route("/api/create_data", methods=["GET"])
# Creates database
def create_data():
    data_sets = ["TRAIN", "TEST"]
    generate_database(data_sets)
    data = generate_data(data_sets)
    # data_json = [x.to_json() for x in data_dict]
    # data_dict["TRAIN"].to_json()
    return jsonify({"action": "success", "data": data})


@app.route("/api/train_model", methods=["GET"])
# Trains model
def train_model():
    conn = sqlite3.connect(db_file)
    select_query = "select * from TRAIN;"
    data = pd.read_sql_query(select_query, conn)

    TRAIN_INPUT = data[["0", "1", "2"]]
    TRAIN_OUTPUT = data[["3"]]

    predictor = LinearRegression(n_jobs=-1)
    predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)

    filename = model_file
    pickle.dump(predictor, open(filename, "wb"))

    model_coefs = dict(enumerate(predictor.coef_.flatten(), 1))
    return jsonify({"action": "success", "data": model_coefs})


@app.route("/api/score_model_test", methods=["GET"])
# Test model scoring call
def score_model_test():
    filename = model_file
    loaded_model = pickle.load(open(filename, "rb"))

    X_TEST = [[10, 20, 30]]
    outcome = loaded_model.predict(X=X_TEST)

    return jsonify({"action": "success", "time": getTime(), "data": outcome.tolist()})


@app.route("/api/score_dataset", methods=["GET"])
# Score model on dataset
def score_model_dataset():
    filename = model_file
    loaded_model = pickle.load(open(filename, "rb"))

    conn = sqlite3.connect(db_file)
    select_query = "select * from TEST;"
    data = pd.read_sql_query(select_query, conn)

    X_TEST = data[["0", "1", "2"]]
    outcome = loaded_model.predict(X=X_TEST)
    data["pred"] = outcome

    return jsonify({"action": "success", "time": getTime(), "data": data.to_dict()})


# score_model
# http://127.0.0.1:5000/api/score_model?id1=1&id2=2&id3=10000
@app.route("/api/score_model", methods=["GET"])
# Score model on api inputs
def score_model():
    query_parameters = request.args
    id1 = float(query_parameters.get("id1"))
    id2 = float(query_parameters.get("id2"))
    id3 = float(query_parameters.get("id3"))
    X_TEST = [[id1, id2, id3]]

    filename = model_file
    loaded_model = pickle.load(open(filename, "rb"))
    outcome = loaded_model.predict(X=X_TEST)
    return jsonify(
        {"action": "success", "input_data": X_TEST, "output_data": outcome.tolist()}
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500)

# app.run(host="localhost", port=8000, debug=True)
