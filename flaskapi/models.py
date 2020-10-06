"""
This module is models for User and Report
"""
from flaskapi import db
from datetime import datetime


class User(db.Model):
    __table_name__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    update_time = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'create_time': self.create_time,
            'update_time': self.update_time
        }
