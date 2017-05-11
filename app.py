import bottle
from bottle import route, run, template

@route('/')
def index(name):
    return '<b>Hello word!!!</b>'

if __name__ == "__main__":
    run(host='localhost', port=8080)

app = bottle.default_app()

