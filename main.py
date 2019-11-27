from bottle import view
import bottle
from bottle import template
import sqlites3
APP = bottle.Bottle()
@APP.get("/")
def index():
    return "<h1>Success!</h1>"
@APP.route("/a")
def index():
    return "<h1>Success22!</h1>"
@APP.route("/q")
def index():
    return template('index')
if __name__ == '__main__':
    APP.run()

