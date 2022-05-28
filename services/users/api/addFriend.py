from flask_restful import Resource
from webargs.flaskparser import use_kwargs
from webargs import fields
import dbconnection

class AddFriend(Resource):

    @use_kwargs({
      "requester": fields.Str(required=True),
      "addressee": fields.Str(required=True)},
      location="query"
      )
    def post(self, requester, addressee):
        """
        Connection request
        ---
        description: "Logged in user adds a friend."
        parameters:
          - in: query
            name: requester
            description: the username of the requester
          - in: query
            name: addressee
            description: the username of the addressee
        responses:
          200:
            description: accepted
          400:
            description: bad request
        """

        # check whether the addressee exists
        check_querry = "SELECT * FROM users WHERE username = %s"

        connection = dbconnection.connect()
        cursor = dbconnection.create_cursor(connection)
        check_result = dbconnection.select_querry(cursor, check_querry, (addressee,))
        addressee_exists = len(check_result) != 0

        # check whether requester and addressee are already friends
        check_querry = "SELECT * FROM friends WHERE requester = %s AND addressee = %s OR requester = %s AND addressee = %s"
        check_result = dbconnection.select_querry(cursor, check_querry, (requester, addressee, addressee, requester,))
        already_friends = len(check_result) != 0

        if not addressee_exists or already_friends or requester == addressee:
            cursor.close()
            connection.close()
            return {"status": "denied"}, 400

        querry = "INSERT INTO friends VALUES (%s,%s)"

        dbconnection.insert_querry(cursor,querry, (requester, addressee,))
        connection.commit()
        cursor.close()
        connection.close()
        return {"status": "accepted"}, 200
