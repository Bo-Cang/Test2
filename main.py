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
@APP.route("/w")
def index():
    conn = sqlite3.connect('data5.db')
    c = conn.cursor()
    c.execute("SELECT * FROM data5 WHERE id = '1000'")
    result = c.fetchall()
    return str(result)
if __name__ == '__main__':
    APP.run()

