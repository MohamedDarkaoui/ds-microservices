from tabnanny import check
from tokenize import group
from flask_restful import Resource
from webargs.flaskparser import use_kwargs
from webargs import fields
import dbconnection

class AddFriendToGroup(Resource):

    @use_kwargs({
      "groupname": fields.Str(required=True),
      "username": fields.Str(required=True),
      "friendname": fields.Str(required=True)},
      location="query"
      )
    def post(self, groupname, username, friendname):
        """
        Connection request
        ---
        description: "Logged in user adds a friend."
        parameters:
          - in: query
            name: groupname
            description: the name of the group
          - in: query
            name: username
            description: the username of the current user
          - in: query
            name: friendname
            description: the username of the friend
        responses:
          200:
            description: accepted
          400:
            description: bad request
        """

        connection = dbconnection.connect()
        cursor = dbconnection.create_cursor(connection)

        # check whether username and friendname are friends
        check_querry = "SELECT * FROM friends WHERE requester = %s AND addressee = %s OR requester = %s AND addressee = %s"
        check_result = dbconnection.select_querry(cursor, check_querry, (username, friendname, friendname, username,))
        are_friends = len(check_result) != 0

        # check whether the group exists
        check_querry = "SELECT * FROM groups WHERE groupname = %s"
        check_result = dbconnection.select_querry(cursor, check_querry, (groupname,))
        group_exists = len(check_result) != 0

        # check whether username is in the group
        check_querry =  "SELECT * FROM group_members WHERE groupname = %s AND member = %s"
        check_result = dbconnection.select_querry(cursor, check_querry, (groupname, username,))
        user_in_group = len(check_result) != 0

        # check whether friendname is in the group
        check_querry =  "SELECT * FROM group_members WHERE groupname = %s AND member = %s"
        check_result = dbconnection.select_querry(cursor, check_querry, (groupname, friendname,))
        friend_in_group = len(check_result) != 0

        if not (are_friends and group_exists and user_in_group and not friend_in_group):
            cursor.close()
            connection.close()
            return {"status": "denied"}, 400

        # add friends to group
        querry = "INSERT INTO group_members VALUES (%s, %s)"
        dbconnection.insert_querry(cursor, querry, (groupname, friendname,))
        connection.commit()
        cursor.close()
        connection.close()
        return {"status": "accepted"}, 200
