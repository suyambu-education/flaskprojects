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

application.run(debug=True,host="0.0.0.0",port=4244)