import os
import re
from datetime import datetime

from flask import current_app as app
from bleach import clean, linkify
from markdown import markdown


class BlogPost():
    """Saves/retrieves blog posts from the blog post folder."""

    def __init__(self, filename, *args, **kwargs):
        """Load a post from a file."""

        path = os.path.join(app.config['POST_PATH'], filename)

        self.title, ext = os.path.splitext(filename)
        self.safe_title = re.sub('[^A-Za-z0-9]', '_', self.title).lower()
        self.timestamp = datetime.fromtimestamp(os.path.getmtime(path))
        with open(path) as f:
            self.body = f.read()
        self.html = linkify(clean(
            markdown(self.body, output_format='html'),
            tags=app.config['OK_HTML'],
            strip=True
        ))

    @staticmethod
    def find(safe_title=None):
        """
        Look through the post directory and return what we find. Optionally,
        return only a post matching the specified title.
        """

        rv = []

        for f in os.listdir(app.config['POST_PATH']):
            name, ext = os.path.splitext(f)
            if ext == '.txt':
                rv.append(BlogPost(f))

        if safe_title:
            for post in rv:
                if post.safe_title == safe_title:
                    return post
            return None

        return rv

