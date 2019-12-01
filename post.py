"""
    Post to database server.
"""
__author__ = 'Hunter'

import uuid
import datetime

from database import Database

"""
    Class: Post
    Param: {int} blog_id, {String} title, {String} content, {datetime} function, {int} id=None
    Descr: Posts a blog to the database server. 
           Currently running MongoDB 4.2.1
"""


class Post(object):

    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.id = uuid.uuid4().hex if id is None else id

    # post = Post(blog_id="123", title="a title", content="some content", author="Hunter", datetime.datetime.utcnow())
    def saveToMongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    def json(self):
        # creates a json representation of the post itself
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }

    @classmethod
    def fromMongo(cls, id):
        post_data = Database.find_one(collection='posts', query={'id': id})
        return cls(blog_id=post_data['blog_id'],
                   title=post_data['title'],
                   content=post_data['content'],
                   author=post_data['author'],
                   date=post_data['created_date'],
                   id=post_data['id']
        )

    @staticmethod
    def fromBlog(id):
        # return Database.find(collection='posts', query={'blog_id': id})
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]
