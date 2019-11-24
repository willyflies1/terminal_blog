"""
    * Application to be used to intereact with MongoDB
    * Date: 11/24/19
    * Copyright, 2019 Hunter Files, All rights reserved.
"""

#import pymongo

from database import Database
from post import Post

__author__ = 'Hunter Files'

Database.initialize()

blog = Blog(author='Hunter',
            title='Sample title',
            description='Description')

blog.new_post()

blog.save_to_mongo()
