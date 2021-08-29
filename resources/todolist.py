from flask import request, jsonify
from flask_restful import Resource, reqparse

class Todo(Resource):
    def get(self, name):
        todolist = TodoListModel.find_by_name(todolistname)
        if todolist:
            return todolist.json()
        return {'message': 'List not found'}, 404

    def post(self, name):
        if TodoListModel.find_by_name(todolistname):
            return {'message': "A store with name '{}' already exists.".format(name)}, 400

        todolist = TodoListModel(todolistname)
        try:
            todolist.save_to_db()
        except:
            return {"message": "An error occurred creating the store."}, 500

        return store.json(), 201

    def delete(self, name):
        todolist = TodoListModel.find_by_name(todolistname)
        if todolist:
            todolist.delete_from_db()

        return {'message': 'todolist deleted'}

class TodoList(Resource):
    def get(self):
        return {'todolist': [todo.json() for todolist in TodoListModel.query.all()]}