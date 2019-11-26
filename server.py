from bottle import view
import bottle
from bottle import template

APP = bottle.Bottle()
@APP.get("/")
def index():
    return "<h1>Success!</h1>"

@APP.get("/q")
@APP.views()
def dd():
    return template('./views/sear.tpl', info)

if __name__ == '__main__':
    bottle.run(application=APP)

