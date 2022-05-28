from flask import Flask
from flask_restful import Api
from flasgger  import Swagger
from api.moviesList import MoviesList

app = Flask(__name__)
api = Api(app)
api.add_resource(MoviesList, '/api/movies')
swage = Swagger(app)


if __name__ == "__main__":
    app.run(host="0.0.0.0")

