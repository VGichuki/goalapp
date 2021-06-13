from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required
from . forms import UpdateProfile, UploadPitch, CommentsForm
from .. import  db
from ..models import User, Pitch, Category,Votes,Comment

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - 60seconds of truth'
    return render_template('index.html', title = title)

@main.route('/pitch')
def pitch():
    pitches = Pitch.query.filter_by().first()

    return render_template('pitch.html', pitches = pitches)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

