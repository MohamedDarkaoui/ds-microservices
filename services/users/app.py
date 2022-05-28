from flask import Flask
from flask_restful import Api
from api.login import Login
from api.register import Register
from api.addFriend import AddFriend
from api.createGroup import CreateGroup
from api.addFriendToGroup import AddFriendToGroup
from flasgger  import Swagger

app = Flask(__name__)
api = Api(app)
swage = Swagger(app)
api.add_resource(Login, '/api/login')
api.add_resource(Register, '/api/register')
api.add_resource(AddFriend, '/api/add-friend')
api.add_resource(CreateGroup, '/api/create-group')
api.add_resource(AddFriendToGroup, '/api/add-friend-to-group')

if __name__ == "__main__":
    app.run(host="0.0.0.0")