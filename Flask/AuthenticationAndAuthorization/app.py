from flask import Flask, render_template, redirect, url_for, request, flash
# Flask (framework para criar aplicações web em Python)
# render_template (usado para renderizar templates HTML dinâmicos utilizando Jinja2)
# redirect (redireciona o navegador do cliente para uma URL específica)
# url_for (gera URLs para funções definidas na aplicação Flask)
# request (contém dados da solicitação HTTP atual, incluindo parâmetros enviados na requisição)

from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user

# LoginManager (classe para gerenciar a autenticação de usuários e suas sessões)
# UserMixin (classe mixin que fornece implementações padrão para métodos necessários em um modelo de usuário)
# login_required (decorador que protege uma rota, permitindo acesso somente a usuários autenticados)
# login_user (função que autentica um usuário e atualiza a sessão do Flask com o ID do usuário)
# logout_user (função que encerra a sessão do usuário autenticado, fazendo o logout)
# current_user (proxy que aponta para o objeto do usuário atualmente autenticado)

app = Flask(__name__)
# (Cria uma instância da aplicação Flask)
app.secret_key = 'supersecretkey'
# (Define uma chave secreta para a segurança da aplicação)
login_manager = LoginManager()
# (Cria uma instância do LoginManager para gerenciar a autenticação)
login_manager.init_app(app)


# (Inicializa o LoginManager com a aplicação Flask)

class User(UserMixin):
    # (Define uma classe de usuário com métodos padrão, fornecidos pelo UserMixin)
    def __init__(self, id):
        self.id = id

    @staticmethod
    def get(user_id):
        # (Método estático para simular a recuperação de um usuário do banco de dados)
        if user_id == "1":
            return User(user_id)
        return None


@login_manager.user_loader
def load_user(user_id):
    # (Função que carrega um usuário a partir do ID armazenado na sessão)
    return User.get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # (Rota de login que aceita métodos GET e POST)
    if request.method == 'POST':
        user = User.get(request.form['user_id'])
        if user:
            login_user(user)
            # login_user(user) (Autentica o usuário e atualiza a sessão com seu ID)
            return redirect(url_for('protected'))
            # redirect(url_for('protected')) (Redireciona o usuário para a rota protegida)
        else:
            flash('Invalid user ID. Please try again.', 'error')
    return render_template('login.html')
    # render_template('login.html') (Renderiza o template HTML de login)


@app.route('/logout')
@login_required
def logout():
    # (Rota de logout que encerra a sessão do usuário)
    logout_user()
    # (Faz o logout do usuário)
    return render_template('logout.html')


@app.route('/protected')
@login_required
def protected():
    # (Rota protegida que exibe uma mensagem com o ID do usuário logado)
    return render_template('protected.html', current_user=current_user)
    # current_user.id (Proxy que aponta para o objeto do usuário atualmente autenticado)


if __name__ == '__main__':
    app.run(debug=True)
