
import bottle, Bottle
APP = Bottle()
@APP.route('/')
def index():
    return '<p>Hello</p>'
@APP.route('/q')
def qq():
    return redirect('/h')
@APP.route('/h')
def hello():
    return '<p>Hello in hello 111</p>'
if __name__ == '__main__':
    APP.run(application=APP)
