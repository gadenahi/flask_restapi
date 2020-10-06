"""
This module to run application for flaskapi
"""
from flaskapi import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)


"""
to initialize the db

from flaskapi import db, create_app
app = create_app()
ctx = app.app_context()
ctx.push()
db.create_all()
exit()

OR

python ./instance/db_create.py
"""
