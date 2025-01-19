# app.py
from flask import Flask, render_template, request
from flask import jsonify

app = Flask(__name__)

# Display your index page
@app.route("/")
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def handle_login():
    # In case we ever need this info:
    username = request.form.get('first')
    password = request.form.get('password')

    # Perform more validation or authentication here if needed
    return render_template('main.html', name=username)  # Render the main.html page

@app.route('/timeline')
def timeline():
    # Get timeline data --> realistically we will end up getting the data from the backend
    data = [
    {"documentName": "Resume_Boeing", "positionName": "Software Engineer", "rating": "5/5", "timeOfUpload": "2025-01-01"},
    {"documentName": "Cover_Letter_Microsoft", "positionName": "Data Analyst", "rating": "3/5", "timeOfUpload": "2025-01-02"},
    {"documentName": "Cover_Letter_Boeing", "positionName": "Full Stack Software Developer", "rating": "4/5", "timeOfUpload": "2025-01-02"},
    {"documentName": "Cover_Letter_Apple", "positionName": "Frontend Engineer", "rating": "4.5/5", "timeOfUpload": "2025-01-03"},
    {"documentName": "Resume_Wealthsimple", "positionName": "Frontend Software Developer", "rating": "5/5", "timeOfUpload": "2025-01-05"},
    {"documentName": "Cover_Letter_Salesforce", "positionName": "Backend Developer", "rating": "3.5/5", "timeOfUpload": "2025-01-08"},
    {"documentName": "Resume_Meta", "positionName": "Software Engineer", "rating": "4/5", "timeOfUpload": "2025-01-10"},
    {"documentName": "Cover_Letter_Paypal", "positionName": "Data Engineer", "rating": "4.5/5", "timeOfUpload": "2025-01-10"},
    {"documentName": "Resume_Stripe", "positionName": "Data Analyst", "rating": "2/5", "timeOfUpload": "2025-01-12"},
    {"documentName": "Cover_Letter_NVIDIA.", "positionName": "UI/UX Designer", "rating": "5/5", "timeOfUpload": "2025-01-18"}
]


    # Pass data to the template
    return render_template('timeline.html', timeline_data=data)


# @app.route('/timeline')
# def timeline():
#     return render_template('timeline.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)    