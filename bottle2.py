from bottle import route, run, template, request, static_file, redirect, bottle
APP = bottle.Bottle()
@APP.get('/')
def hello():
    return "hello world in hello"
    
@APP.get('/1/')
def HELLO():
    return redirect("/2/")
@APP.get('/2/')
def hello2():
    return "Hello world in hello2"
if __name__ == '__main__':
    bottle.run(application=APP)
