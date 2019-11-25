
from bottle import route, run
from bottle import template,view, bottle
APP = bottle.Bottle()
@APP.get('/info')
@APP.view('info.html')
def info():
        name = '戴儒锋'
        age = '30'
        blog = 'www.linuxyw.com'
        qq = '63780668'
        book = ['python','linux','php']
        price = {'pc':4000,'phone':2000,'bike':600}
        data = {'tname':name,'tage':age,'tblog':blog, 'tqq': qq,'tbook':book,'tprice':price,'tnum':''}
        return data
if __name__ == '__main__':
    bottle.run(application=APP)
