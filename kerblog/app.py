import os
import uuid

import flask

from kerblog.views import views


def create_app(*args, **kwargs):
    """Create a server instance."""

    app = flask.Flask(
        __name__,
        instance_relative_config=True,
        static_url_path='',
        *args, **kwargs)
    if not os.path.exists(app.instance_path):
        os.makedirs(app.instance_path)

    app.config.update(
        SECRET_KEY=str(uuid.uuid4()),
        POST_PATH=os.path.join(app.instance_path, 'posts'),
        OK_HTML=['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                 'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul', 'h1',
                 'h2', 'h3', 'h4', 'h5', 'p']
    )
    config_path = os.path.join(app.instance_path, 'blog.cfg')
    if not os.path.exists(config_path):
        raise RuntimeError(
            'Could not find config file at {p}!'.format(p=config_path)
        )
    app.config.from_pyfile(config_path)

    post_path = app.config['POST_PATH']
    if not os.path.exists(post_path):
        os.makedirs(post_path)

    app.register_blueprint(views)

    return app

