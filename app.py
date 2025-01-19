# app.py
from flask import Flask, render_template, request
from flask import jsonify
import json

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
<<<<<<< HEAD
    # data = [
    #     {"documentName": "Doc 1", "positionName": "Position 1", "rating": "5/5", "timeOfUpload": "2025-01-18"},
    #     {"documentName": "Doc 2", "positionName": "Position 2", "rating": "4.5/5", "timeOfUpload": "2025-01-18"},
    #     {"documentName": "Doc 3", "positionName": "Position 3", "rating": "4/5", "timeOfUpload": "2025-01-18"},
    #     {"documentName": "Doc 4", "positionName": "Position 4", "rating": "4.5/5", "timeOfUpload": "2025-01-18"},
    #     {"documentName": "Doc 5", "positionName": "Position 5", "rating": "5/5", "timeOfUpload": "2025-01-18"},
    #     {"documentName": "Doc 6", "positionName": "Position 1", "rating": "5/5", "timeOfUpload": "2025-01-18"},
    #     {"documentName": "Doc 7", "positionName": "Position 2", "rating": "4.5/5", "timeOfUpload": "2025-01-18"},
    #     {"documentName": "Doc 8", "positionName": "Position 3", "rating": "4/5", "timeOfUpload": "2025-01-18"},
    #     {"documentName": "Doc 9", "positionName": "Position 4", "rating": "4.5/5", "timeOfUpload": "2025-01-18"},
    #     {"documentName": "Doc 10", "positionName": "Position 5", "rating": "5/5", "timeOfUpload": "2025-01-18"},
    # ]
=======
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
>>>>>>> ef82dc0fb8099a6be26e7c5059021ee65ab69767


    # Pass data to the template
    # return render_template('timeline.html', timeline_data=data)
    fastapi_url = "http://127.0.0.1:8001/retrieve_db_entries"

    # Define the payload with the required user_name
    payload = {"user_name": "desired_user_name"}

    try:
        # Make a POST request to the FastAPI endpoint
        response = request.post(fastapi_url, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Extract the result from the JSON response
        result = response.json().get("result", "[]")

        # Convert the JSON string back to a Python list
        timeline_data = json.loads(result)

    except request.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        print(f"An error occurred: {e}")
        timeline_data = []

    # Pass the data to the template
    return render_template('timeline.html', timeline_data=timeline_data)


# @app.route('/timeline')
# def timeline():
#     return render_template('timeline.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)    