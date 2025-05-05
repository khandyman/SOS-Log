from flask import Flask, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return "<h1>Hello World</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# @app.route('/hello', methods=['GET', 'POST'])
# def hello():
#     if request.method == 'GET':
#         return 'You made a GET request\n'
#     elif request.method == 'POST':
#         return 'You made a POST request\n'
#     else:
#         return 'You will never see this message\n'
#
#
# @app.route('/greet/<name>')
# def greet(name):
#     return f"Hello {name}"
#
#
# @app.route('/add/<int:num1>/<int:num2>')
# def add(num1, num2):
#     return f"{num1} + {num2} = {num1 + num2}"
#
#
# @app.route('/handle_url_params')
# def handle_url_params():
#     if 'name' in request.args.keys() and 'greeting' in request.args.keys():
#         name = request.args['name']
#         greeting = request.args.get('greeting')
#
#         return f"{greeting}, {name}"
#     else:
#         return f"Some parameters are missing"
