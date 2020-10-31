# Importing all the packages
from flask import Flask
from flask import request, render_template
import requests

# Flask App
app = Flask(__name__)

# Route to the home page
@app.route('/', methods=["GET", "POST"])
def index():
    # Rendering to the home page
    return render_template("home.html")

# Routes for Ajax Call
@app.route('/ajax_call', methods=["GET", "POST"])
def ajax_call():
    # to get the data from the Flask app and using get if key might not exist
    data = request.form.get("data")
    # URL to data from backend
    url = "http://127.0.0.1:4000/autocomplete?query="+str(data)
    # Asking a GET request and returning a response object
    response = requests.request("GET", url, data = data)
    # return json response to elasticsearch
    return response.json()

# Run Flask App
if __name__ == "__main__":
    app.run(debug=True, port=5000)
