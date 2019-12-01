"""
    * Application to be used to intereact with MongoDB
    * Date: 11/24/19
    * Copyright, 2019 Hunter Files, All rights reserved.
"""

#import pymongo
from blog import Blog
from database import Database
from menu import Menu
# from post import Post
from post import Post

__author__ = 'Hunter Files'


"""Works to save a blog to posts collection
Database.initialize()

post = Post(blog_id="80245",
            title='Student lunch number',
            content='My identification code for food',
            author=__author__)
post.saveToMongo()

"""

Database.initialize()

menu = Menu()
menu.run_menu()