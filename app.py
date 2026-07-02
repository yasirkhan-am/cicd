import os
from flask import Flask

app = Flask(__name__)

PORT = int(os.getenv("PORT", 8000))

@app.route("/")
def home():
    return "Hello python python app"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
