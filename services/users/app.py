from flask import Flask
from flask_restful import Api
from api.login import Login
from api.register import Register
from flasgger  import Swagger

app = Flask(__name__)
api = Api(app)
swage = Swagger(app)
api.add_resource(Login, '/api/login')
api.add_resource(Register, '/api/register')

if __name__ == "__main__":
    app.run(host="0.0.0.0")