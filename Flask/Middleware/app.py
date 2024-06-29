from flask import Flask

app = Flask(__name__)


# @app.route('/', method=['POST'])
# def

@app.before_request
def before_request():
    print("Before request")


@app.after_request
def after_request(response):
    print("After request")
    return response


if __name__ == '__main__':
    app.run(debug=True, port=3000)
