from flask_restful import Resource
from webargs.flaskparser import use_kwargs
from webargs import fields
from api import users
import dbconnection

class Login(Resource):

    @use_kwargs({
      "username": fields.Str(required=True),
      "password": fields.Str(required=True)},
      location="query"
      )
    def get(self, username, password):
        """
        Connection request
        ---
        description: "Checks whether the username and password combination exists."
        parameters:
          - in: query
            name: username
            description: the username
          - in: query
            name: password
            description: the password
        responses:
          200:
            description: Exists
          401:
            description: Does not exist
        """
        querry = "SELECT * FROM users WHERE username = %s and password = %s"
        params = (username, password)

        connection = dbconnection.connect()
        cursor = dbconnection.create_cursor(connection)
        result = dbconnection.select_querry(cursor, querry, params)
        cursor.close()
        connection.close()

        if len(result) != 0:
          return {"status" : "accepted"}, 200

        return {"status": "denied"}, 401
