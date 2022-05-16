from flask import Flask, jsonify, send_file
import requests
import json
import csv

app = Flask(__name__)


def get_all_characters() -> json:
    url = "https://rickandmortyapi.com/api/character/?Species=Human&status=alive&origin=earth"

    characters_list = requests.get(url).json()["results"]  # get all the results of the query
    return characters_list


def get_character_info() -> list:
    characters_list = get_all_characters()
    character_info = list()

    for character in characters_list:
        character_info.append(
            {"name": character["name"], "location": character["origin"]["name"], "image": character["image"]})

    return character_info


def write_to_csv(rows: list):
    header = ['name', 'location', 'image']

    with open("./rickandmorty_CSV.csv", "w") as csv_file:
        # write the Headers to to the csv file
        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)


def get_csv() -> str:
    write_to_csv(get_character_info())
    return "./rickandmorty_CSV.csv"


# health check for the api
@app.route("/healthcheck")
def healthcheck():
    return "<h1>This API is live</h1>"


# fetch json from the api
@app.route("/fetch")
def fetch_data():
    return jsonify(get_character_info())


# download the csv file generated by the api
@app.route("/download_csv")
def download_csv():
    return send_file(get_csv(), as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
