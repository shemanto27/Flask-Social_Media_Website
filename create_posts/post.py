from flask import Blueprint, render_template

post = Blueprint('post', __name__, static_folder='static', template_folder='templates')

@post.route('/')
def post():
    return render_template('post.html')