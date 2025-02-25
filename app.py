from flask import Flask, render_template, jsonify, request
from bulk_page_add import *
from dotenv import load_dotenv
import os
import io
import csv


app = Flask(__name__)

load_dotenv()
API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")


@app.route('/')
def index_page():

    return render_template('index.html')



@app.route('/upload_csv', methods=['post'])
def csv_upload():
    if 'csv_file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['csv_file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # read csv file
    stream = io.StringIO(file.stream.read().decode('utf-8'))
    csv_reader = csv.DictReader(stream)

    # grabbing only column named subject_code
    subject_codes = [row['subject_code'] for row in csv_reader]

    # converting to string to send to view
    subject_codes_string = ",".join(subject_codes)
    
    return render_template('load_from_file.html', subjects = subject_codes_string)



@app.route('/add_page', methods=['post'])
def process_add_page():

    # fetching form data
    data = request.form

    # instatiating object to process bulk add
    bulk_add = BulkPageAdd(API_URL, API_KEY, data['content'], data['subjects'])

    status = bulk_add.bulk_add_pages()

    if status == 1:
        to_render = render_template('success.html', add = data['subjects'])
    else:
        to_render = render_template('failure.html')

    return to_render

if __name__ == '__main__':
    app.run(debug=False)