from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask! This is home page"

@app.route("/welcome")
def home():
    return "Welcome Page"

@app.route("/contact")
def contact():
    return "Contact Us"

if __name__ == "__main__":
    app.run(debug=True)