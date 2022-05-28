from flask_restful import Resource
from webargs.flaskparser import use_kwargs
from webargs import fields
import dbconnection


class Register(Resource):

    @use_kwargs({
      "username": fields.Str(required=True),
      "password": fields.Str(required=True)},
      location="query"
      )
    def post(self, username, password):
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
        check_querry = "SELECT * FROM users WHERE username = %s"
        check_params = tuple(username)

        querry = "INSERT INTO users VALUES (%s,%s)"
        params = (username, password)

        connection = dbconnection.connect()
        cursor = dbconnection.create_cursor(connection)
        check_result = dbconnection.select_querry(cursor, check_querry, check_params)


        if len(check_result) != 0:
          cursor.close()
          connection.close()
          return {"status" : "denied"}, 401
        dbconnection.insert_querry(cursor, querry, params)
        connection.commit()
        cursor.close()
        connection.close()
        return {"status": "accepted"}, 200