from flask import Flask, jsonify,  render_template
from database import get_student_records

app = Flask(__name__)

@app.route('/')
def contact_form():
    records = get_student_records()
    return render_template("home.html", records = records)