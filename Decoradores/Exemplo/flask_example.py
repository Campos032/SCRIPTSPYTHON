from flask import Flask

app = Flask(__name__)


@app.route('/home')
def homepage():
    return 'Essa é minha HomePage'


@app.route('/login')
def login():
    return f'Seu Login'


app.run(port=3000)
