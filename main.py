from bottle import view
import bottle
from bottle import template
import sqlite3
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
    conn = sqlite3.connect('data5.db')
    c = conn.cursor()
    sql = "select * " \
        + "from page_info  " \
        + "where id in " + id_list + ";"
    res = c.execute(sql)
    res = [r for r in res]
    return res
if __name__ == '__main__':
    APP.run()

