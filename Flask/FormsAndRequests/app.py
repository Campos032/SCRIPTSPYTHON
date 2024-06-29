from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return f"Username: {username}, Password: {password}"
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
