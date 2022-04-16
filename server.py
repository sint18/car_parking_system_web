
import datetime
from flask import Flask, redirect, request, session, url_for, render_template, jsonify
import secrets
import functions
import queries
import variables

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)

log = queries.log
# login & logout


@app.route("/", methods=["GET", "POST"])
def login():

    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = functions.get_hash(request.form["password"])
        record = queries.login(username, password)
        if record:
            if record[4] == "active":
                session["u_id"] = record[0]
                session["user"] = record[2]

                # logging
                log(record[0], f"{record[2]} logged in successfully")

            else:
                error = "Account is deactivated"
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

    print()
    data = {
        "parked_vehicles": f"{queries.count_parked_vehicles()}/{variables.PARKING_LIMIT}",
        "categories": queries.count_categories(),
        "history": queries.count_history(),
        "over_parked": queries.count_over_parked(variables.TIME_LIMIT)
    }
    return render_template("dashboard.html", data=data)

# user_management/users


@app.route("/user-management", methods=["GET", "POST"])
def user_management():
    if "user" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        u_id = request.form["formUserId"]
        status = request.form["formStatus"]
        queries.update_user_status(u_id, status)

        # logging
        if status == "active":
            msg = f"{session['user']} activated the user with the id ''{u_id}''"
            log(session["u_id"], msg)
        elif status == "inactive":
            msg = f"{session['user']} deactivated the user with the id ''{u_id}''"
            log(session["u_id"], msg)

    data = []
    records = queries.get_user_list()
    if records:
        data = records
    return render_template("user_management.html", data=data)


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

                # logging
                msg = f"{session['user']} added a new admin with the username ''{username}''"
                log(session["u_id"], msg)

        return redirect(url_for("user_management"))

    return render_template("user_management/add_new_user.html")


@app.route("/delete/<ltype>", methods=["GET", "POST"])
def delete(ltype):
    if ltype == "user":
        u_id = request.args.get('u_id')

        if u_id:
            queries.delete_user(int(u_id))

            # logging
            msg = f"{session['user']} deleted the user with the id ''{u_id}''"
            log(session["u_id"], msg)

        return redirect(url_for("user_management"))

    elif ltype == "category":
        c_id = request.args.get("c_id")
        if c_id:
            queries.delete_category(c_id)

            # logging
            msg = f"{session['user']} deleted the category with the id ''{c_id}''"
            log(session["u_id"], msg)

        return redirect(url_for("category"))

    elif ltype == "activity":
        act_id = request.args.get("act_id")
        if act_id:
            queries.delete_activity(act_id)
        return redirect(url_for("activity_log"))

    elif ltype == "all-activity":
        queries.clear_history()
        return redirect(url_for("activity_log"))

    elif ltype == "coupon":
        coupon_id = request.args.get("coupon_id")
        if coupon_id:
            queries.delete_coupon(coupon_id)

            # logging
            msg = f"{session['user']} deleted the coupon with the id ''{coupon_id}''"
            log(session["u_id"], msg)

        return redirect(url_for("coupons"))


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

                # logging
                msg = f"{session['user']} updated the details of the user with the id ''{u_id}''"
                log(session["u_id"], msg)

                return redirect(url_for("user_management"))
            elif new_pass and old_pass and fullname and username:
                if functions.get_hash(old_pass) == record[0][3]:
                    queries.update_user(
                        u_id, fullname, username, functions.get_hash(new_pass))

                    # logging
                    msg = f"{session['user']} updated the password of the user with the id ''{u_id}''"
                    log(session["u_id"], msg)

                    return redirect(url_for("user_management"))
                else:
                    error = "Incorrect old password"

        return render_template("user_management/edit_user.html", data=record[0], error=error)

    if ltype == "category":
        error = None
        c_id = request.args.get("c_id")
        record = queries.get_category_by_id(c_id)

        if request.method == "POST":
            cat_name = request.form["category_name"]
            cat_desc = request.form["desc"]

            queries.update_category(c_id, cat_name, cat_desc)

            # logging
            msg = f"{session['user']} updated the category with the id ''{c_id}''"
            log(session["u_id"], msg)

            return redirect(url_for("category"))

        return render_template("category/edit_category.html", data=record[0])

    elif ltype == "coupon":
        coupon_id = request.args.get("coupon_id")
        if request.method == "POST":
            coupon_code = request.form["coupon_code"]
            discount = request.form["discount"]

            queries.update_coupon(coupon_id, coupon_code, discount)

            # logging
            msg = f"{session['user']} updated the coupon with the id ''{coupon_id}''"
            log(session["u_id"], msg)

            return redirect(url_for("coupons"))

        record = queries.get_coupon_by_id(coupon_id)
        return render_template("coupon/edit_coupon.html", data=record)

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

            # logging
            msg = f"{session['user']} added a new category with the name ''{cat_name}''"
            log(session["u_id"], msg)

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
        other["remark"] = "Over Parked"
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
    if request.method == "POST":
        cat_id = request.form["cat_id"]
        reg_num = request.form["reg_num"]
        if cat_id != "" and reg_num != "":
            queries.insert_vehicles(cat_id, reg_num)
            msg = f"New vehicle added with the reg no. {reg_num}"

            # logging
            msg = f"{session['user']} added a new vehicle with the reg no. ''{reg_num}''"
            log(session["u_id"], msg)

    return redirect(url_for("vehicles", msg=msg))


@app.route("/update-vehicle", methods=["GET", "POST"])
def update_vehicle():
    if "user" not in session:
        return redirect(url_for("login"))

    vehicle_id = request.args.get("v_id")
    record = queries.get_parked_vehicles_by_id(vehicle_id)
    entry_time = record[3]  # entry time
    exit_time = record[4]  # exit time

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
    member_info = queries.get_member_info_by_id(record[2])
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

        # logging
        msg = f"{session['user']} updated vehicle with the reg no. ''{record[2]}'' for out-going"
        log(session["u_id"], msg)

        return redirect(url_for("vehicles"))

    return render_template("vehicles/update_vehicle.html", data=record, fees=functions.format_currency(fees), other=other)

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
    m_status = []
    status = "inactive"
    if records:
        for row in records:
            new_list = list(row)

            ddiff = row[4] - datetime.date.today()
            cost = functions.format_currency(row[7])
            if ddiff.days <= 0:
                m_status.append("inactive")
            else:
                m_status.append("active")
            new_list.extend([ddiff, cost])
            data.append(tuple(new_list))

    if "active" in m_status:
        status = "active"

    return render_template("members/member_info.html", data=data, msg=msg, status=status)


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

        # logging
        msg = f"{session['user']} added a tier id ''{tier_id}'' membership for the reg no. ''{reg_no}''"
        log(session["u_id"], msg)

    return redirect(url_for("view_members"))
    # records = queries.get_tiers()
    # return render_template("members/register_member.html", data=records, msg=msg)


@app.route("/terminate-membership", methods=["GET", "POST"])
def terminate_membership():
    if request.method == "POST":
        ms_id = request.form["selectMembershipId"]
        queries.revoke_membership(ms_id)

        # logging
        msg = f"{session['user']} terminated membership with the membership id ''{ms_id}''"
        log(session["u_id"], msg)

    return redirect(url_for("view_members"))


@app.route("/view-tiers", methods=["GET", "POST"])
def view_tiers():

    if request.method == "POST":
        tierName = request.form["tierName"]
        discount = request.form["discount"]
        price = request.form["price"]
        queries.insert_tier(tierName, price, discount)

    tier_records = queries.get_tiers()
    tier_data = []
    for row in tier_records:
        data = list(row)
        data[2] = functions.format_currency(row[2])
        tier_data.append(data)
    return render_template("members/view_tiers.html", tier_data=tier_data)


@app.route("/get-tier/<t_id>")
def get_tier(t_id):
    tier_record = queries.get_tier_by_id(t_id)
    print(tier_record)
    return jsonify(tier_record)


@app.route("/update-tier", methods=["GET", "POST"])
def update_tier():
    if request.method == "POST":
        tier_id = request.form["selectTierId"]
        tierName = request.form["tierName"]
        discount = request.form["discount"]
        price = request.form["price"]

        if tier_id:
            queries.update_tier(tier_id, tierName, price, discount)

    return redirect(url_for("view_tiers"))


# activity log


@app.route("/activity-log")
def activity_log():
    admin_id = session["u_id"]
    records = queries.get_activity_by_admin_id(admin_id)
    return render_template("activity_log/activity_log.html", admin_log=records)


# coupons

@app.route("/coupon-management", methods=["GET", "POST"])
def coupons():

    if request.method == "POST":
        c_status = request.form["formStatus"]
        c_id = request.form["formCouponId"]
        queries.update_coupon_status(c_id, c_status)

        # logging
        if c_status == "active":
            msg = f"{session['user']} activated the coupon with the id ''{c_id}''"
            log(session["u_id"], msg)
        elif c_status == "expired":
            msg = f"{session['user']} deactivated the coupon with the id ''{c_id}''"
            log(session["u_id"], msg)

    data = queries.get_coupons()
    return render_template("coupons.html", data=data)


@app.route("/create-coupon", methods=["GET", "POST"])
def new_coupon():
    if request.method == "POST":
        coupon_code = request.form["coupon_code"].upper()
        discount = request.form["discount"]
        queries.insert_coupon(coupon_code, discount)

        # logging
        msg = f"{session['user']} created a new coupon ''{coupon_code}''"
        log(session["u_id"], msg)

        return redirect(url_for("coupons"))

    return render_template("coupon/add_new_coupon.html")


if __name__ == "__main__":
    app.run(debug=True)
