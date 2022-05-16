from flask import Flask
import random
app = Flask(__name__)

print(random.__name__)
print(__name__)

# here "/" means homepage
# this is python decorators


def bold_fun(fun):
    def wrapper_fun():
        return "<b>"+fun()+"</b>"
    return wrapper_fun


def em_fun(fun):
    def wrapper_fun():
        return "<em>"+fun()+"</em>"
    return wrapper_fun


def underlined_fun(fun):
    def wrapper_fun():
        return "<u>"+fun()+"</u>"
    return wrapper_fun


@app.route('/')
def hello_world():
    return "<h1 style='text-align:center'>hello, world!</h1><p>this is sakurai</p>" \
           "<img src='https://cdn.myanimelist.net/images/characters/3/39188.webp'><br>" \
           "<img src='https://media0.giphy.com/media/nR4L10XlJcSeQ/200.webp?" \
           "cid=ecf05e47ky9vyijssz68mqm29w4fyycug2t28wk5dqbrborl&rid=200.webp'>"


@app.route("/bye")
@underlined_fun
@bold_fun
@em_fun
def bye_world():
    return "bye"


@app.route("/<name>/<int:number>")
# this can be used to pull the path after name in browser.
@app.route("/<path:name>")
def greet(name, number):
    return f"hello {name}. you are {number} year old"


if __name__ == "__main__":
    # run app in debug mode to auto reload the server.
    app.run(debug=True)
