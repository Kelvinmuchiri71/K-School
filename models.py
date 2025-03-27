from flask_sqlalchemy import SQLAlchemy                                      #we are importing a constructor class from the flask_sqlalchemy package
from flask_migrate import Migrate
from sqlalchemy_serializer import SerializerMixin


db = SQLAlchemy()                                                          #our database takes in one argument

migrate = Migrate()                                                      #tracks the schema


class Student(db.Model, SerializerMixin):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    pass

def to_dict(self):
    return {"id": self.id, "name": self.name}



# class Teacher(db.Model, SerializerMixin):

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)

#     pass