
import bottle
from bottle import redirect
APP = bottle.Bottle()
@APP.get('/')
def index():
    return '<p>Hello</p>'
@APP.get('/q')
def qq():
    redirect('/h')
@APP.get('/h')
def hello():
    return '<p>Hello in hello 111</p>'
if __name__ == '__main__':
    bottle.run(application=APP)
