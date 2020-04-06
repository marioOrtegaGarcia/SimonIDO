from project import app

from flask import render_template, redirect, url_for

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/dashboard.html")

@app.route("/admin")
def admin():
    return redirect(url_for("admin_dashboard"))
