# app.py
from flask import Flask, render_template
from flask import jsonify

app = Flask(__name__)

# Display your index page
@app.route("/")
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def handle_login():
    # In case we ever need this info:
    # username = request.form.get('first')
    # password = request.form.get('password')

    # Perform more validation or authentication here if needed
    return render_template('main.html')  # Render the main.html page


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)    