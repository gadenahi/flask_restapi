import os
import sys

print('Creating database tables for User app...')

if os.path.abspath(os.curdir) not in sys.path:
    print('...missing directory in PYTHONPATH... added!')
    print('os.curdir', os.path.abspath(os.curdir))
    sys.path.append(os.path.abspath(os.curdir))


from flaskapi import db, create_app


app = create_app()
ctx = app.app_context()
ctx.push()
db.drop_all()
db.create_all()
exit()
