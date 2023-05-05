from flask import Flask, render_template, redirect, url_for
from flask import request
import csv

app = Flask(__name__)

# Make routes for each HTML file
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

# Allow user to submit data
@app.route("/submit_form", methods=['POST'])
def submit_form():
    
    # Check request data has arrived properly
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data, "contact_data.csv")
            return redirect("thankyou.html")
        except:
            return redirect(url_for("error.html", error_message="Your contact data could not be saved"))
    else:
        return redirect(url_for("error.html", error_message="An error ocurred"))

# Write contact info in data file
def write_to_csv(data, filename):
    
    with open(filename, mode="a", newline="") as cv:
        
        email = data.get("email", "")
        subject = data.get("subject", "")
        message = data.get("message", "")
        
        csv_writer = csv.writer(cv, 
                                delimiter=",", 
                                quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)
        
        csv_writer.writerow([email, subject, message])