from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, FileField, SelectField
from wtforms.validators import DataRequired, URL, Email, ValidationError, Length
from flask_wtf.file import FileRequired
from flask_ckeditor import CKEditorField
import email_validator


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle")
    img_url = StringField("Blog Image URL")
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("SIGN ME UP!")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("LET ME IN!")


class CommentForm(FlaskForm):
    comment_text = TextAreaField("Comment", validators=[DataRequired()], render_kw={'class': "form-control", "rows":5})
    submit = SubmitField("SUBMIT COMMENT")


class ContactForm(FlaskForm):
    username = StringField("Name", validators=[DataRequired()], render_kw={'class': "form-control", "placeholder": "Name"})
    email = StringField("Email Address", validators=[DataRequired(), Email()], render_kw={'class': "form-control", "placeholder": "Email Address"})
    phone_number = StringField("Phone Number", render_kw={'class': "form-control", "placeholder": "Phone Number"})
    message = TextAreaField("Message", validators=[DataRequired()], render_kw={'class': "form-control", "placeholder": "Message", "rows":5})
    submit = SubmitField("SEND")


class UploadImageForm(FlaskForm):
    file = FileField("Opload an image", validators=[FileRequired()], render_kw={'accept': "image/*"})
    submit = SubmitField("Upload")

    def validate_file(form, field):
        if not field.data.mimetype.startswith("image"):
            raise ValidationError("Invalid file type, image only.")


class UploadFileForm(FlaskForm):
    file = FileField("Opload a file", validators=[FileRequired()])
    submit = SubmitField("Upload")


class AddFriendForm(FlaskForm):
    friend_id = SelectField('Friend Name', validators=[DataRequired()])


class NewGroupForm(FlaskForm):
    group_name = StringField("Group Name", validators=[DataRequired(), Length(max=25)])
    group_member = SelectField('Friend Name', validators=[DataRequired()])


class AddMemberForm(FlaskForm):
    group_name = SelectField("Group Name", validators=[DataRequired()])
    group_member = SelectField('New Member Name', validators=[DataRequired()])
