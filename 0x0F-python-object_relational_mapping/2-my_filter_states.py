#!/usr/bin/python3
"""Module that connects to a MySQL server and retrieves information
from the database.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    user_name = argv[1]
    pass_word = argv[2]
    data_base = argv[3]
    search_name = argv[4]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=user_name,
                         passwd=pass_word,
                         db=data_base)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE CONVERT(`name` USING Latin1) COLLATE Latin1_General_CS = '%s';", search_name)
    states = cursor.fetchall()
    for state in states:
        print(state)
