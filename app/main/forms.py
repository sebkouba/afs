from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


class TopicForm(Form):
    summary = StringField('Summary', validators=[Required()])
    description = TextAreaField('Description')
    submit = SubmitField('Save')
