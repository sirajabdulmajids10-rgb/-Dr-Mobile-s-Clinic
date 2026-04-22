from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Dr. Mobile’s Clinic</h1><p>Website is working ✅</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
