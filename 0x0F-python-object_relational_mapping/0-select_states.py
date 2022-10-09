#!/usr/bin/python3

import MySQLdb
from sys import argv

user_name = argv[1]
pass_word = argv[2]
data_base = argv[3]

db = MySQLdb.connect(host="localhost",
                     port=3306,
                     user=user_name,
                     passwd=pass_word,
                     db=data_base)
cursor = db.cursor()

cursor.execute("SELECT * FROM states ORDER BY id")
states = cursor.fetchall()
for state in states:
    print(state)
