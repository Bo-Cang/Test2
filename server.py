from bottle import view
import bottle
from bottle import template

APP = bottle.Bottle()
@APP.get("/")
def index():
    return "<h1>Success!</h1>"

@APP.get("/q")
def dd():
    template('./views/sear.tpl', context)

if __name__ == '__main__':
    bottle.run(application=APP)

