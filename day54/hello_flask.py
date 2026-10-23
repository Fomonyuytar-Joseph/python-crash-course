from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/login")
def login():
    return "<h1>Login user 123</h1>"


@app.route("/< >")
def greet(name):
    return f"Hello there {name}"

if __name__ == '__main__':
    app.run(debug=True)