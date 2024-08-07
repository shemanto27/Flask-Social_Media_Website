from flask import Blueprint, render_template

newsfeed = Blueprint('newsfeed', __name__, static_folder='static', template_folder='templates')

@post.route('/')
def post():
    return render_template('newsfeed.html')