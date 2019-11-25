
import bottle
APP = bottle.Bottle()
@APP.get('/')
def index():
    return '<p>Hello</p>'
@APP.get('/1/')
def re():
    return redirect("/hello/")
@APP.get('/hello/')
def index():
    def hello1():
    return '<p>Hello in hello 111</p>'
if __name__ == '__main__':
    bottle.run(application=APP)
