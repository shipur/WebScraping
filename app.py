from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

# create route that renders index.html template
@app.route("/")
def index():
    findings = mongo.db.findings.find_one()
    return render_template("index.html", findings=findings)


@app.route("/scrape")
def scrape():
    findings = mongo.db.findings
    findings_data = scrape_mars.scrape_this()
    # findings.insert_one(findings_data)
    findings.update(
        {},
        findings_data ,
        upsert=True
    )
    # return redirect("http://localhost:5000/", code=302)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)



