from flask import Flask
from flask_restful import Api
from resources.user import User, UserList
from resources.todolist import Todo, TodoList


app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/todo_api"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'anythingyouwant'
api = Api(app)

api.add_resource(User, '/user/<string:username>')
api.add_resource(Todo, '/todolist/<string:todolistname>')
api.add_resource(UserList, '/users')
api.add_resource(TodoList, '/todolists')


if __name__ == '__main__':
    from db import db
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)