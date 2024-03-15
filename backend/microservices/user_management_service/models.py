from enum import Enum
import sqlalchemy
from . import db


class Role(Enum):
    FARMER = 0
    NONFARMER = 1

    def __str__(self):
        return self.name


class User(db.Model):
    __tablename__ = "maga_user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    phone_number = db.Column(db.String(12))
    email_address = db.Column(db.String(100))
    password = db.Column(db.String(100))
    role = db.Column(sqlalchemy.types.Enum(Role))
    farmer_pid = db.Column(db.String(20))
    profile_bio = db.Column(db.Text)

    def __init__(self, name, phoneNumber, emailAddress, password, role, profileBio, farmer_pid=None):
        self.name = name
        self.phone_number = phoneNumber
        self.email_address = emailAddress
        self.password = password
        self.role = role
        self.farmer_pid = farmer_pid
        self.profile_bio = profileBio

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone_number': self.phone_number,
            'email_address': self.email_address,
            'role': str(self.role),
            'farmer_pid': self.farmer_pid,
            'profile_bio': self.profile_bio
        }