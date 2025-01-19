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
        {"documentName": "Doc 1", "positionName": "Position 1", "rating": "5/5", "timeOfUpload": "2025-01-18"},
        {"documentName": "Doc 2", "positionName": "Position 2", "rating": "4.5/5", "timeOfUpload": "2025-01-18"},
        {"documentName": "Doc 3", "positionName": "Position 3", "rating": "4/5", "timeOfUpload": "2025-01-18"},
        {"documentName": "Doc 4", "positionName": "Position 4", "rating": "4.5/5", "timeOfUpload": "2025-01-18"},
        {"documentName": "Doc 5", "positionName": "Position 5", "rating": "5/5", "timeOfUpload": "2025-01-18"},
        {"documentName": "Doc 6", "positionName": "Position 1", "rating": "5/5", "timeOfUpload": "2025-01-18"},
        {"documentName": "Doc 7", "positionName": "Position 2", "rating": "4.5/5", "timeOfUpload": "2025-01-18"},
        {"documentName": "Doc 8", "positionName": "Position 3", "rating": "4/5", "timeOfUpload": "2025-01-18"},
        {"documentName": "Doc 9", "positionName": "Position 4", "rating": "4.5/5", "timeOfUpload": "2025-01-18"},
        {"documentName": "Doc 10", "positionName": "Position 5", "rating": "5/5", "timeOfUpload": "2025-01-18"},
    ]

    # Pass data to the template
    return render_template('timeline.html', timeline_data=data)


# @app.route('/timeline')
# def timeline():
#     return render_template('timeline.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)    