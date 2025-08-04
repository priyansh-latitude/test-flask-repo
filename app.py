from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello, Flask!"

@app.route("/home")
def home():
    return "Home Page"

if __name__ == "__main__":
    app.run(debug=True)