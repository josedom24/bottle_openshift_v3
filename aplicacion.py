from bottle import route, run, template

@route('/')
def index(name):
    return '<b>Hello word!!!</b>'

