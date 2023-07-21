# app.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_location_data(ip_address, api_key):
    base_url = "http://api.ipstack.com/"
    response = requests.get(f"{base_url}{ip_address}?access_key={api_key}")
    data = response.json()
    return data

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        api_key = "9ce8b397770fc47a4d764a3de74cd8c6"  # Replace 'YOUR_API_KEY' with your actual Ipstack API key
        ip_address = request.form["ip_address"]
        location_data = get_location_data(ip_address, api_key)
        
        if "error" in location_data:
            error_message = location_data["error"]["info"]
            return render_template("index.html", error_message=error_message)
        else:
            return render_template("index.html", location_data=location_data)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
