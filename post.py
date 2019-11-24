"""
    Create an objet called Post

"""

class Post(object):

    def __init__(self, blog_id, title, content, author, date, id):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.id = id

        def saveToMongo(self):
            Database.insert(collection='posts',
                            query=self.json())
            pass

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