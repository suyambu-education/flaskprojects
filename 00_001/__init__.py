from flask import Flask
from flask import render_template
application=Flask(__name__)
@application.route("/")
@application.route("/home")
def index():
    return render_template("index.html")
@application.route("/About")
@application.route("/about")
def about():
    return render_template("about.html")
@application.route("/Service")
@application.route("/service")
def service():
    return render_template("service.html")
@application.route("/Portfolio")
def portfolio():
    return render_template("portfolio.html")
@application.route("/Contact")
def contact():
    return render_template("contact.html")
@application.route("/exam-login")
@application.route("/examlogin")
def exam_login():
    return render_template("exam/exam-login.html")
@application.route("/admin-login")
@application.route("/adminlogin")
def admin_login():
    return render_template("admin/admin-login.html")


application.run(debug=True,host="0.0.0.0",port=4244)