from flask_restful import Resource
from webargs.flaskparser import use_kwargs
from webargs import fields
import dbconnection

class CreateGroup(Resource):

    @use_kwargs({
      "administrator": fields.Str(required=True),
      "groupname": fields.Str(required=True)},
      location="query"
      )
    def post(self, administrator, groupname):
        """
        Connection request
        ---
        description: "Logged-in user creates a group."
        parameters:
          - in: query
            name: administrator
            description: the username of the logged-in user
          - in: query
            name: groupname
            description: the name of the new group
        responses:
          200:
            description: accepted
          400:
            description: bad request
        """
        # check whether a group with the same name already exists
        check_querry = "SELECT * FROM groups WHERE groupname = %s"

        connection = dbconnection.connect()
        cursor = dbconnection.create_cursor(connection)
        check_result = dbconnection.select_querry(cursor, str(check_querry), (groupname,))
        groupname_exists = len(check_result) != 0

        if groupname_exists:
            cursor.close()
            connection.close()
            return {"status": "denied"}, 400

        querry = "INSERT INTO groups VALUES (%s,%s)"
        querry2 = "INSERT INTO group_members VALUES (%s,%s)"
        dbconnection.insert_querry(cursor, querry, (administrator, groupname,))
        dbconnection.insert_querry(cursor, querry2, (groupname, administrator,))
        connection.commit()
        cursor.close()
        connection.close()
        return {"status" : "accepted"}, 200