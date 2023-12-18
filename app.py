
from flask import Flask, render_template


app = Flask (__name__)


@app.route("/")
def hello_world():
    return render_template ("home.html")

@app.route("/about")
def abouttt():
    return "<p> abouttttt, world!</p>"

@app.route("/second")
def wasssap():
    return render_template ("second.html")

if __name__ == "__main__":
    app.run(debug=True)