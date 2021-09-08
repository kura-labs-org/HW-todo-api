from datetime import datetime
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://@localhost:5432/todo_app"
db = SQLAlchemy(app)
api = Api(app)
migrate = Migrate(app, db)

class UserModel(db.Model):
    __tablename__ = 'users'


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250))
    password = db.Column(db.String(15))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    todolist = db.relationship('TodoListModel', backref='user_model', cascade='all, delete, delete-orphan', single_parent=True , lazy='dynamic')

    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def json(self):
        return {'username': self.username, 'todolist': [todolist.json() for todolist in self.todolist.all()]}

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
        return user

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

class TodoListModel(db.Model):
    __tablename__ = 'todolists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    name = db.Column(db.String(250))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    items = db.relationship('TodoListItemModel', backref='todo_list_model', cascade='all, delete, delete-orphan', single_parent=True , lazy='dynamic')
    Completed = db.Column(db.Boolean, default=False, nullable=False)
    usermodel_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)


    def __init__(self, name):
        self.name = todolistname
        self.description = description
    
    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

class TodoListItemModel(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    itemname = db.Column(db.String(250))
    usermodel_id = db.Column(db.Integer, db.ForeignKey('todolists.id'),
        nullable=False)


    def __init__(self, todolistname, todolisttext):
        self.itemname = itemname
        self.todolistdescription = todolistdescription

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

class User(Resource):
    """
    this is to parse the responses that we get from the body or payloadd

    """
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="create a username"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="create a password"
    )
    
    def get(self, username):
        user = UserModel.find_by_username(username)
        if user:
            return user.json()
        return 404
    
    def post(self, username):
        if UserModel.find_by_username(username):
            return {'message': " user '{}' already exists.".format(username)}, 400

        data = User.parser.parse_args()

        # **data enter all the data passed as in the body like a spread operator or @bodyParam in java, or *Kwargs
        user = UserModel(**data)

        try:
            user.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return user.json(), 201
    
    def put(self, username):
        data = User.parser.parse_args()

        user = UserModel.find_by_username(username)

        if user is None:
            user = UserModel(name, **data)
        else:
            user.username = data['username']
            user.password = data['password']

        item.save_to_db()

        return item.json()
    
    def delete(self, username):
        user = UserModel.find_by_username(username)
        if user:
            username.delete_from_db()

        return {'message': 'user deleted'}


class UserList(Resource):
    def get(self):
        return {'users': [user.json() for user in UserModel.query.all()]}

class TodoList(Resource):
    """
    this is to parse the responses that we get from the body or payloadd

    """
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="provide a name"
    )
    
    def get(self, name):
        todo = TodoListModel.find_by_name(name)
        if todo:
            return todo.json()
        return 404
    
    def post(self, name):
        if TodoListModel.find_by_name(username):
            return {'message': " list '{}' already exists.".format(name)}, 400

        data = TodoList.parser.parse_args()

        # **data enter all the data passed as in the body like a spread operator or @bodyParam in java, or *Kwargs
        todo = TodoListModel(name, **data)

        try:
            todo.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return todo.json(), 201
    
    def put(self, username):
        data = TodoList.parser.parse_args()

        todo =TodoListModel.find_by_name(username)

        if todo is None:
            todo = TodoListModel(name, **data)
        else:
            todo.name = data['name']

        todo.save_to_db()

        return todo.json()
    
    def delete(self, name):
        todo = TodoListModel.find_by_name(name)
        if todo:
            todo.delete_from_db()

        return {'message': 'user deleted'}


class TodoLists(Resource):
    def get(self):
        return {'users': [todolist.json() for todolist in TodoListModel.query.all()]}
        

api.add_resource(User, '/users/<string:username>')
api.add_resource(UserList, '/users')
api.add_resource(TodoList, '/lists/<string:name>')
api.add_resource(TodoLists, '/lists')


if __name__ == "__main__":
    app.run(debug=True)
