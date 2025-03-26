from flask_sqlalchemy import SQLAlchemy                                      #we are importing a constructor class from the flask_sqlalchemy package
from flask import Flask
from flask_migrate import Migrate
from sqlalchemy_serializer import SerializerMixin

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False                           #tracks all modifications

db = SQLAlchemy(app)                                                          #our database takes in one argument

migrate = Migrate(app,db)                                                      #tracks the schema


class Student(db.Model, SerializerMixin):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    pass

class Teacher(db.Model, SerializerMixin):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    pass