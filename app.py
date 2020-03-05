# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.
from flask import Flask, render_template, jsonify

app = Flask(__name__)

data = [
    {"ime": "Janez", "velikost": 126},
    {"ime": "Miha", "velikost": 345},
    {"ime": "Polde", "velikost": 321},
    {"ime": "Lojze", "velikost": 176}
]


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")

# #######################
# API
# #######################


@app.route("/api/v1/data", methods=["GET"])
def get_data():
    return jsonify(data)


@app.route("/api/v1/find/<name>")
def find_person(name):
    try:
        d = [x for x in data if x["ime"] == name][0]
    except IndexError as exc:
        return jsonify({"error": str(exc)})
    # d = None
    # for x in data:
    #     if x["ime"] == name:
    #         d = x
    #         break
    return jsonify(d)


if __name__ == '__main__':
    app.run(debug=True)
