import os

import flask
from flask import Flask, render_template
from livereload import Server

app = Flask(__name__, static_folder='public/', template_folder='templates/')
app.debug = True
server = Server(app.wsgi_app)
cd = os.path.dirname(__file__)
server.watch(cd)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    # app.run()
    server.serve()
