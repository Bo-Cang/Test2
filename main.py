from bottle import view
import bottle
from bottle import template
APP = bottle.Bottle()
@APP.get("/")
def index():
    return "<h1>Success!</h1>"
@APP.route("/a")
def index():
    return "<h1>Success22!</h1>"
@APP.route("/q")
def index():
    return template('index2')
if __name__ == '__main__':
    APP.run()

