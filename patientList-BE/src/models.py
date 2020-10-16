from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from src import db, login_manager, bcrypt
from flask_login import UserMixin
from marshmallow import fields, Schema

# additions @ postgresql
from flask_serialize import FlaskSerializeMixin

FlaskSerializeMixin.db = db


class User(db.Model, FlaskSerializeMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    saab = db.Column(db.String(1), nullable=False) #sex assigned at birth
    nik = db.Column(db.String(16), nullable=False, default="0123456789ABCDEF")
    cell_no = db.Column(db.String(), nullable=False, default='08xxxxxxxxxx')
    address = db.Column(db.String(), nullable=False, default='Jalan Tuhan')
    religion = db.Column(db.String(), nullable=False, default='Ketuhanan Yang Maha Esa')
    education = db.Column(db.String(), nullable=False, default='Jalan Ilmu')
    blood_type = db.Column(db.String(), nullable=False, default='A')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    modified_at = db.Column(db.DateTime, default=datetime.utcnow)
    

    __tablename__ = 'users'


    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        print("HELLO, THIS IS USER CONSTRUCTOR")
        print("test one, what is username?")
        # print(data.get('username'))
        self.name = data.get('name')
        self.nik = data.get('nik')
        self.saab = data.get('saab')
        self.cell_no = data.get('cell_no')
        self.address = data.get('address') 
        self.religion = data.get('religion')
        self.education = data.get('education')
        self.blood_type = data.get('blood_type')   
        self.created_at = datetime.utcnow()
        self.modified_at = datetime.utcnow()

    

    def save(self):
        db.session.add(self)
        db.session.commit()


    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.utcnow()
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()


    @staticmethod
    def get_all():
        return User.query.all()


    @staticmethod
    def get_one(id):
        return User.query.get(id)

    # serialize to JSON, STATIC METHOD
    @staticmethod
    def as_dict(thing):
       return {c.name: getattr(thing, c.name) for c in thing.__table__.columns}
    