from flask import Flask
from flask_cors import CORS

# import route handler
from ascii_upload import ascii_upload
from git_webhook import git_webhook 


# Create Flask App
app = Flask(__name__)

# ***** using CORS in Python Everywhere cause errors *****
# # Enable CORS for requests from your local frontend (or allow all origins for testing)
CORS(app)


# Routers
@app.route("/")
def home():
    return "Hello world"

# git hub webhook 
# Trigger then git updated
@app.route("/webhook", methods=["POST"]) 
def handle_webhook():
    return git_webhook()

@app.route("/ascii/upload", methods=["POST"])
def handle_ascii_upload():
    return ascii_upload()


# Run app if only if in current directory
if __name__ == "__main__":
    app.run(debug=True)

# [TEST] This should be auto updated on python anywhere