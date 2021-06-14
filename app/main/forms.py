from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required,length, DataRequired
from flask_wtf.file import FileField,file_allowed

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators = [Required()])
    submit = SubmitField('Submit')

class UploadPitch(FlaskForm):
    title = StringField('Tiltle')
    # bio = TextAreaField('Tell us about yourself.',validators = [Required()])
    submit = SubmitField('Submit')
    category=SelectField('Select Category',validators=[DataRequired()],choices=[('Advertisement','Advertisement'),('Interview','Interview'),('Products','Products'),('IT','IT'),('Political','Political'),('Pickup Lines','Pickup Lines')])
    pitch=TextAreaField('Write Pitch:',validators=[DataRequired()])
    submit=SubmitField('Post Pitch')

class CommentsForm(FlaskForm):
    comment=TextAreaField('Type comment:', validators=[DataRequired()])
    submit=SubmitField('Post Comment')

