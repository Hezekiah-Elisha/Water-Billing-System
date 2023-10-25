# from wtforms import Form, StringField, IntegerField, validators
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired


class SupervisorForm(FlaskForm):
    user_id = IntegerField('User ID', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])