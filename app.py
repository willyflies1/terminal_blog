"""
    * Application to be used to intereact with MongoDB
    * Date: 11/24/19
    * Copyright, 2019 Hunter Files, All rights reserved.
"""
import pymongo

from database import Database
from post import Post

__author__ = 'Hunter Files'

Database.initialize()


post = Post("Title: ", "Content: ", "Author: ")                   # create an instance of a Post(object)
post2 = Post("Title: A Title", "Content: Some content", "Author: Hunter")

print(post.content)
print(post2.author)