from bottle import route, run, static_file, view
import bottle
from bottle import template

APP = bottle.Bottle
@APP.get("/")
def index():
    return "<h1>Success!</h1>"

@APP.get("/q")
def dd():
    return template('sear.tpl', info)

if __name__ == '__main__':
    bottle.run(application=APP)

