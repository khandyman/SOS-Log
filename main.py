from flask import Flask
from classes.flask_app import FlaskApp
from classes.routes import Routes

app = Flask(__name__, template_folder='templates')
flask_app = FlaskApp(app)
routes = Routes(app)

flask_app.add_endpoint('/', 'index', routes.totals, methods=['GET'])
flask_app.add_endpoint('/totals', 'index', routes.totals, methods=['GET'])
flask_app.add_endpoint('/ep_log', 'ep_log', routes.ep_log, methods=['GET'])
flask_app.add_endpoint('/gp_log', 'gp_log', routes.gp_log, methods=['GET'])

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', debug=True)

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
