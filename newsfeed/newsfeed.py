from flask import Blueprint, render_template

newsfeed = Blueprint('newsfeed', __name__, static_folder='static', template_folder='templates')

@newsfeed.route('/')
def show_newsfeed():
    return render_template('newsfeed.html')
