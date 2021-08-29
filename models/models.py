from db import db

class UserModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250))
    password = db.Column(db.String(15))
    addresses = db.relationship('TodoListModel', backref='usermodel', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
        return user

class TodoListModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    todolistname = db.Column(db.String(250))
    todolisttext = db.Column(db.String(1000))
    usermodel_id = db.Column(db.Integer, db.ForeignKey('usermodel.id'),
        nullable=False)


    def __init__(self, todolistname, todolisttext):
        self.todolistname = todolistname
        self.todolisttext = todolisttext
