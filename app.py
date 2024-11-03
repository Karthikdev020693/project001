from flask import Flask
from waitress import serve
from controller.home import home


app = Flask(__name__)

app.register_blueprint(home)


if __name__ == '__main__':
   #app.run(host='0.0.0.0', port='4300', debug=True)

   serve(app, host='0.0.0.0', port=4300)