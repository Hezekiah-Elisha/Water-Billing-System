import os
from app import create_app, db
# from app.auth.models import User, TokenBlocklist
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
# app = create_app('default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db)
