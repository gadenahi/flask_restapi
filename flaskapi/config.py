"""
Setting for SQL server
"""

import os


class Config:
    """
    Setting for SQL server
    """
    # .bash-profile
    SECRET_KEY = os.environ.get('SECRET_KEY')
    WTF_CSRF_SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
