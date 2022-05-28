from flask_restful import Resource
from webargs.flaskparser import use_kwargs
from webargs import fields
import psycopg2

class MoviesList(Resource):

    def get(self):
        """
        Connection request
        ---
        description: "Gets a list of all movies."
        responses:
          200:
            description: accepted
          500:
            description: error
        """
        try:
          connection = psycopg2.connect(
            host="movies-db", port="5432",
            database="movies", user="postgres",
            password = "postgres"
          )
          cursor = connection.cursor()
          querry = "SELECT Title FROM movies"
          cursor.execute(querry)
          result = cursor.fetchall()

          cursor.close()
          connection.close()

          result = [movie[0] for movie in result]

          return {"movies": result}, 200

        except:
          return {"movies:": []}, 500