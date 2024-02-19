#!/usr/bin/python3
"""This script retrieves all states whose names start
with the letter 'N'"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = "localhost"
    port = 3306
    db = MySQLdb.connect(host=host, user=username, passwd=password,
                         db=db_name, port=port)
    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE name REGEXP "^N.*" ORDER BY states.id ASC')
    result = cur.fetchall()
    cur.close()
    db.close()
    if result:
        for row in result:
            if row[1][0] == "N": # Filter results to ensure only states starting with "N" are displayed
                print(row)
