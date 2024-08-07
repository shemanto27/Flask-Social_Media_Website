from flask import Flask
from create_posts.post import post
from newsfeed.newsfeed import newsfeed

app = Flask(__name__)
app.register_blueprint(post, url_prefix='/post')
app.register_blueprint(newsfeed, url_prefix='/newsfeed')

if __name__ == "__main__":
    app.run(debug=True)
