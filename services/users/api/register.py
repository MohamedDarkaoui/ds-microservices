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
        description: "Adds a new user to the database."
        parameters:
          - in: query
            name: username
            description: the username
          - in: query
            name: password
            description: the password
        responses:
          200:
            description: accepted
          401:
            description: unauthorized
        """
        check_querry = "SELECT * FROM users WHERE username = %s"

        querry = "INSERT INTO users VALUES (%s,%s)"

        #check if user already exists
        connection = dbconnection.connect()
        cursor = dbconnection.create_cursor(connection)
        check_result = dbconnection.select_querry(cursor, check_querry, (username,))

        if len(check_result) != 0:
          cursor.close()
          connection.close()
          return {"status" : "denied"}, 401

        #add user
        dbconnection.insert_querry(cursor, querry, (username, password,))
        connection.commit()
        cursor.close()
        connection.close()
        return {"status": "accepted"}, 200