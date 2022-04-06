from crypt import methods
from sre_parse import FLAGS
from flask import Flask, flash, redirect, request, session, url_for, render_template, jsonify
import secrets
import functions
import queries


app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)


@app.route("/", methods=["GET", "POST"])
def login():

    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = functions.get_hash(request.form["password"])
        record = queries.login(username, password)
        if record:
            for row in record:
                session["u_id"] = row[0]
                session["user"] = row[2]
        else:
            error = "Invalid credentials, try again"

    if "user" in session:
        return redirect(url_for("dashboard"))
    return render_template("login.html", error=error)


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html")


@app.route("/settings", methods=["GET", "POST"])
def settings():
    if "user" not in session:
        return redirect(url_for("login"))

    data = []
    records = queries.get_user_list()
    if records:
        data = records
    return render_template("settings.html", data=data)


@app.route("/add-user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        fullname = request.form["fullname"]
        username = request.form["username"]
        password = request.form["password"]
        con_password = request.form["confirm_password"]

        if fullname != "" and username != "" and password != "" and con_password != "":
            if password == con_password:
                queries.insert_user(fullname, username,
                                    functions.get_hash(password))

                return redirect(url_for("settings"))

    return render_template("settings/add_new_user.html")


@app.route("/delete/<type>", methods=["GET", "POST"])
def delete(type):
    if type == "user":
        u_id = request.args.get('u_id')

        if u_id:
            queries.delete_user(int(u_id))
    return redirect(url_for("settings"))


@app.route("/edit/<type>", methods=["GET", "POST"])
def edit(type):
    if type == "user":
        error = None
        u_id = request.args.get('u_id')
        data = []
        record = queries.get_user_by_id(u_id)

        if request.method == "POST":
            fullname = request.form["fullname"]
            username = request.form["username"]
            new_pass = request.form["new_password"]
            old_pass = request.form["old_password"]

            if not new_pass and not old_pass and fullname and username:
                queries.update_user(u_id, fullname, username)
                return redirect(url_for("settings"))
            elif new_pass and old_pass and fullname and username:
                if functions.get_hash(old_pass) == record[0][3]:
                    queries.update_user(
                        u_id, fullname, username, functions.get_hash(new_pass))
                    return redirect(url_for("settings"))
                else:
                    error = "Incorrect old password"

        return render_template("settings/edit_user.html", data=record[0], error=error)


@app.route("/vehicles")
def vehicles():
    if "user" not in session:
        return redirect(url_for("login"))

    records = queries.get_parked_vehicles()
    return render_template("vehicles/vehicles.html", data=records)


@app.route("/vehicle-entry", methods=["GET", "POST"])
def vehicle_entry():
    if "user" not in session:
        return redirect(url_for("login"))
    msg = None
    categories = queries.get_categories()
    if request.method == "POST":
        cat_id = request.form["cat_id"]
        reg_num = request.form["reg_num"]
        if cat_id != "" and reg_num != "":
            queries.insert_vehicles(cat_id, reg_num)
            msg = f"New vehicle added with the reg no. {reg_num}"
    return render_template("vehicles/vehicle_entry.html", data=categories, msg=msg)


@app.route("/update-vehicle")
def update_vehicle():
    if "user" not in session:
        return redirect(url_for("login"))

    vehicle_id = request.args.get("v_id")
    record = queries.get_parked_vehicles_by_id(vehicle_id)
    entry = record[0][3]  # entry time
    exit = record[0][4]  # exit time
    tdiff = exit - entry
    fees = "test"
    return render_template("vehicles/update_vehicle.html", data=record[0], fees=fees)


@ app.route("/logout")
def logout():
    session.pop("user")
    session.pop("u_id")
    if "user" not in session:
        return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
