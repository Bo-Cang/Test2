from bottle import route, run, template, request, static_file, redirect, bottle
APP = bottle.Bottle()
@APP.get('/')
def index():
    return 'hello world in hello'
if __name__ == '__main__':
    bottle.run(application=APP)
