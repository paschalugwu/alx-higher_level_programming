#!/usr/bin/python3
"""This script lists all the states from the db"""

import MySQLdb
import sys

if __name__ == "__main__":
    """List all states in db"""
    username = "root"
    password = "benziopax"
    db_name = "hbtn_0e_0_usa"
    host = "localhost"
    port = 3306
    db = MySQLdb.connect(host=host, user=username, passwd=password,
                         db=db_name, port=port)
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC;')
    result = cur.fetchall()
    cur.close()
    db.close()
    if result:
        for row in result:
            print(row)
