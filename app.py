import bottle
from bottle import route, run, template

@route('/')
def index(name):
    return '<b>Hello word!!!</b>'

if __name__ == "__main__":
	run(host='0.0.0.0', port=8080, server='gunicorn', workers=4)

app = bottle.default_app()

