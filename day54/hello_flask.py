from flask import Flask

app = Flask(__name__)


def make_bold(fn):
    def wrapper_function():
        content = fn()
        return f"<b>{content}</b>"
    return wrapper_function


@app.route("/")
def hello_world():
    return (
        "<h1 style='text-align:center'>Hello, World!</h1>"
        "<p>This is a paragraph</p>"
    )

@app.route("/bye")
@make_bold
# @make_emphasis
# @make_underlined
def bye():
    return "Bye!"

@app.route("/login") 
def login():
    return "<h1>Login user 123</h1>"


@app.route("/<name>")
def greet(name):
    return f"Hello there {name}"

if __name__ == '__main__':
    app.run(debug=True)