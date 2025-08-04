from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello, Flask!"

@app.route("/home")
def home():
    return "Home Page"

@app.route("/contact")
def contact():
    return "Contact Us"

if __name__ == "__main__":
    app.run(debug=True)