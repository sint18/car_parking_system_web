from sre_parse import FLAGS
from flask import Flask, flash, redirect, request, session, url_for, render_template, jsonify
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)


@app.route("/", methods=["GET", "POST"])
def login():

    error = None
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
