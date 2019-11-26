from bottle import route, run, static_file, view
import bottle

APP = bottle.Bottle
@APP.get("/")
def index():
    return "<h1>Success!</h1>"

@APP.get("/q")
@view("home")
def example_template_render():
    return {"now": dt.now().isoformat()}

if __name__ == '__main__':
    bottle.run(application=APP)

