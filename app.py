from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    return "Starting Machine learning project"


if __name__ == "__main__":
    app.run(debug = True)