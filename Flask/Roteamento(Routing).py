# . Roteamento (Routing)
# O roteamento em Flask é a maneira como definimos URLs e vinculamos essas URLs a funções Python.

# Exemplo Básico:
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, Flask!"


if __name__ == '__main__':
    app.run(debug=True)


# Aqui, definimos a rota /, que é a URL raiz. Quando um usuário acessa essa URL, a função home é executada e retorna
# "Hello, Flask!".

# Parâmetros na URL:
# Podemos capturar partes da URL como parâmetros.
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'
# A URL /user/john chamará a função show_user_profile com username definido como 'john'.
