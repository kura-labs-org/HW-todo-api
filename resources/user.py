from flask import request, jsonify
from flask_restful import Resource, reqparse
  

class User(Resource):
    """
    get a user
    """
    def getUser(self, name):
        user = UserModel.find_by_name(username)
        if user:
            return user.json()
        return 404

    """
    create a user
    """
    def createUser(self, name):
        if UserModel.find_by_name(username):
            return {'message': "A User with name '{}' already exists.".format(username)}, 400

        user = UserModel(name)
        try:
            User.save_to_db()
        except:
            return {"message": "An error occurred creating the user."}, 500

        return user.json(), 201


     """
    delete a user
    """
     def delete(self, name):
        user = UserModel.find_by_name(username)
        if user:
            username.delete_from_db()

        return {'message': 'user deleted'}

class UserList(Resource):
    def get(self):
        return {'users': [user.json() for user in UserModel.query.all()]}
