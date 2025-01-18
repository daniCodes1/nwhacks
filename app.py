# app.py
from flask import Flask, render_template
from flask import jsonify

app = Flask(__name__)

# Display your index page
@app.route("/")
def index():
    return render_template('login.html')

@app.route("/concatenate")
def concatenate():
    # Could also just get it from frontend just an eg of routing
    str1 = "Adrian"
    str2 = "Michael"
    str3 = "Rishabh"
    result = str1 + " " + str2 + " " + str3
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)    