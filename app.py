"""
    * Application to be used to intereact with MongoDB
    * Date: 11/24/19
    * Copyright, 2019 Hunter Files, All rights reserved.
"""
import pymongo

__author__ = 'Hunter Files'

uri = "mongodb://127.0.0.1:27017"       # where on the server we are connecting to
client = pymongo.MongoClient(uri)       # creates a client object to interact
database = client['fullstack']          # database we are modifying
collection = database['students']       # collection we are modifying


students = [student for student in collection.find({}) if student['Mark'] == 99.0]
print(students)

"""
students = collection.find({})          # would find all the data in the collection
student_list = []
# print(students) shows the Cursor object
for student in students:                # list comprehension
    student_list.append(student)        # add each student to a list
"""