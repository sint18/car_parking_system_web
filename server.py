
import datetime
from flask import Flask, redirect, request, session, url_for, render_template, jsonify
import secrets
import functions
import queries
import variables

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)


# login & logout
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


@ app.route("/logout")
def logout():
    session.pop("user")
    session.pop("u_id")
    if "user" not in session:
        return redirect(url_for("login"))


# dashboard
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    data = {
        "parked_vehicles": f"{queries.count_parked_vehicles()}/{variables.PARKING_LIMIT}",
        "categories": queries.count_categories(),
        "history": queries.count_history(),
        "over_parked": queries.count_over_parked(variables.TIME_LIMIT)
    }
    return render_template("dashboard.html", data=data)

# settings/users


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


@app.route("/delete/<ltype>", methods=["GET", "POST"])
def delete(ltype):
    if ltype == "user":
        u_id = request.args.get('u_id')

        if u_id:
            queries.delete_user(int(u_id))
        return redirect(url_for("settings"))

    if ltype == "category":
        c_id = request.args.get("c_id")
        if c_id:
            queries.delete_category(c_id)
        return redirect(url_for("category"))


@app.route("/edit/<ltype>", methods=["GET", "POST"])
def edit(ltype):
    if ltype == "user":
        error = None
        u_id = request.args.get('u_id')
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

    if ltype == "category":
        error = None
        c_id = request.args.get("c_id")
        record = queries.get_category_by_id(c_id)

        if request.method == "POST":
            cat_name = request.form["category_name"]
            cat_desc = request.form["desc"]

            queries.update_category(c_id, cat_name, cat_desc)
            return redirect(url_for("category"))

        return render_template("category/edit_category.html", data=record[0])

# category


@app.route("/categories")
def category():
    if "user" not in session:
        return redirect(url_for("login"))

    records = queries.get_categories()
    return render_template("category/category.html", data=records)


@app.route("/add-category", methods=["GET", "POST"])
def add_category():
    if "user" not in session:
        return redirect(url_for("login"))
    msg = None

    if request.method == "POST":
        cat_name = request.form["category_name"]
        cat_desc = request.form["desc"]
        if cat_name:
            queries.insert_category(cat_name, cat_desc)
            return redirect(url_for("category"))

    return render_template("category/add_new_category.html", msg=msg)

# vehicles


@app.route("/parking-history")
def parking_history():
    if "user" not in session:
        return redirect(url_for("login"))

    records = queries.get_vehicle_history()
    return render_template("vehicles/parking_history.html", data=records)


@app.route("/vehicle-info")
def view_info():
    if "user" not in session:
        return redirect(url_for("login"))

    other = {
        "remark": "",
        "fine": 0,
        "membership": []
    }
    v_id = request.args.get("v_id")
    record = queries.get_vehicle_info_by_id(int(v_id))
    member_info = queries.get_member_info_by_id(record[1])
    if member_info:
        member_status = member_info[2]
        if member_status == "active":
            other["membership"].extend(
                ["Active", member_info[4], member_info[3], member_info[6], member_info[7]])
    if record[7]:
        other["fine"] = functions.format_currency(record[7])
    return render_template("vehicles/vehicle_info.html", data=record, fees=functions.format_currency(record[5]), other=other)


@app.route("/vehicles")
def vehicles():
    if "user" not in session:
        return redirect(url_for("login"))

    vehicle_records = queries.get_parked_vehicles()
    category_records = queries.get_categories()
    return render_template("vehicles/vehicles.html", vehicle_data=vehicle_records, category_data=category_records)


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
    return redirect(url_for("vehicles", msg=msg))


@app.route("/update-vehicle", methods=["GET", "POST"])
def update_vehicle():
    if "user" not in session:
        return redirect(url_for("login"))

    vehicle_id = request.args.get("v_id")
    record = queries.get_parked_vehicles_by_id(vehicle_id)
    entry_time = record[0][3]  # entry time
    exit_time = record[0][4]  # exit time

    rate_1, rate_2 = variables.RATE_1, variables.RATE_2

    tdiff = exit_time - entry_time

    t_limit = datetime.timedelta(hours=24)
    total_hr = tdiff.total_seconds()/3600
    other = {
        "remark": "",
        "fine": 0,
        "membership": []
    }
    fine = None
    fees = functions.calculate_fees(
        total_hr, rate_1, rate_2)
    member_info = queries.get_member_info_by_id(record[0][2])
    if member_info:
        member_status = member_info[2]
        if member_status == "active":
            other["membership"].extend(
                ["Active", member_info[4], member_info[3], member_info[6], member_info[7]])
            discount = member_info[3] / 100
            fees = fees - (fees * discount)
    if tdiff > t_limit:
        fine = variables.FINE
        other["remark"] = "Over Parked"
        other["fine"] = functions.format_currency(variables.FINE)
        fees = fees + fine

    if request.method == "POST":
        queries.update_vehicle(vehicle_id, exit_time,
                               int(fees), tdiff, fine)
        return redirect(url_for("vehicles"))

    return render_template("vehicles/update_vehicle.html", data=record[0], fees=functions.format_currency(fees), other=other)

# members


@app.route("/view-members")
def view_members():

    records_members = queries.get_members()
    tier_records = queries.get_tiers()

    member_list = []
    member_data = []
    if records_members:
        for row in records_members:
            member_data.append((row[0], row[1], row[2]))
            member_list.append(row[0])

    for i in member_list:
        queries.update_status(i)
    return render_template("members/view_members.html", member_data=member_data, tier_data=tier_records)


@app.route("/member-info")
def view_member_info():
    msg = None
    m_id = request.args.get("m_id")
    records = queries.get_member_info(m_id)
    data = []
    if records:
        for row in records:
            new_list = list(row)
            ddiff = row[4] - row[3]
            cost = functions.format_currency(row[7])
            new_list.extend([ddiff, cost])
            data.append(tuple(new_list))

    return render_template("members/member_info.html", data=data, msg=msg)


@app.route("/register-member", methods=["GET", "POST"])
def register_member():

    if request.method == "POST":
        reg_no = request.form["reg_num"]
        tier_id = request.form["tierSel"]
        start_date = request.form["startDate"]
        valid_until = request.form["validUntil"]

        member_records = queries.get_members()
        member_dict = {}
        for row in member_records:
            member_dict[row[1]] = row[0]

        if reg_no in member_dict.keys():
            queries.extend_member(
                member_dict[reg_no], tier_id, start_date, valid_until)
        else:
            queries.register_member(reg_no, tier_id, start_date, valid_until)

            # queries.register_member(reg_no, tier, start_date, valid_until)

    return redirect(url_for("view_members"))
    # records = queries.get_tiers()
    # return render_template("members/register_member.html", data=records, msg=msg)


@app.route("/terminate-membership", methods=["GET", "POST"])
def terminate_membership():
    if request.method == "POST":
        ms_id = request.form["selectMembershipId"]
        queries.revoke_membership(ms_id)
    return redirect(url_for("view_members"))


@app.route("/view-tiers")
def view_tiers():
    tier_records = queries.get_tiers()
    tier_data = []
    for row in tier_records:
        data = list(row)
        data[2] = functions.format_currency(row[2])
        tier_data.append(data)
    return render_template("members/view_tiers.html", tier_data=tier_data)


@app.route("/get-tiers/<t_id>")
def get_tiers(t_id):
    tier_record = queries.get_tier_by_id(t_id)
    print(tier_record)
    return jsonify(tier_record)


if __name__ == "__main__":
    app.run(debug=True)
