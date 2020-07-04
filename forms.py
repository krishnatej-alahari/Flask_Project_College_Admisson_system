from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=10, max=10)])
    password = PasswordField('password', validators=[DataRequired()])
    cpassword = PasswordField('cpassword', validators=[DataRequired(), EqualTo('password')])
    sname = StringField('sname', validators=[DataRequired(), Length(min=5, max=20)])
    score = IntegerField('score', validators=[DataRequired()])
    contact = StringField('contact', validators=[DataRequired()])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=10, max=10)])
    password = PasswordField('password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class AddClgForm(FlaskForm):
    cid = StringField('cid', validators=[DataRequired(), Length(min=5, max=5)])
    cname = StringField('cname', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    website = StringField('website')
    submit = SubmitField('Add College')

class AddCutoffForm(FlaskForm):
    cid = StringField('cid', validators=[DataRequired(), Length(min=5, max=5)])
    bname = StringField('cname', validators=[DataRequired()])
    cyear = IntegerField('cyear', validators=[DataRequired()])
    cutoff = IntegerField('cutoff', validators=[DataRequired()])
    num = IntegerField('num', validators=[DataRequired()])
    submit = SubmitField('AddCutoff')

class ResisterStudentsForm(FlaskForm):
    cid = StringField('cid', validators=[DataRequired(), Length(min=5, max=5)])
    bname = StringField('bname', validators=[DataRequired()])
    uname = StringField('uname', validators=[DataRequired(), Length(min=10, max=10)])
    astatus = StringField('astatus', validators=[DataRequired()])
    submit = SubmitField('Resister Students')

class ApplyClgForm(FlaskForm):
    cid = StringField('cid', validators=[DataRequired(), Length(min=5, max=5)])
    bname = StringField('bname', validators=[DataRequired()])
    submit = SubmitField('Apply College')