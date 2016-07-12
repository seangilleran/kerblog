from datetime import datetime

import flask

from kerblog.models import BlogPost


views = flask.Blueprint('views', __name__)


@views.app_context_processor
def inject_time():
    return dict(timestamp=datetime.now())


@views.route('/')
def index():
    posts = BlogPost.find()
    return flask.render_template('blog.htm', posts=posts, pg='blog')


@views.route('/post/<title>')
def get_post(title):
    post = BlogPost.find(title)
    if not post:
        flask.abort(404)
    return flask.render_template('blog.htm', posts=[post], pg='blog')


@views.route('/cv/')
def cv():
    return flask.render_template('cv.htm', pg='cv')


@views.route('/projects/')
def projects():
    return flask.render_template('projects.htm', pg='projects')

