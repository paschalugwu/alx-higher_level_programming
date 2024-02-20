#!/usr/bin/python3

import MySQLdb
import sys


def filter_states(mysql_username, mysql_password, db_name, state_name):
    """
    Filter states by user input.

    Args:
        mysql_username (str): MySQL username.
        mysql_password (str): MySQL password.
        db_name (str): Database name.
        state_name (str): State name to search.

    Returns:
        None
    """
    # Establish a connection to the MySQL server
    connection = MySQLdb.connect(
        user=mysql_username,
        password=mysql_password,
        host='localhost',
        port=3306,
        db=db_name
    )

    # Create a cursor object
    cursor = connection.cursor()

    # Construct the SQL query
    query = "SELECT * FROM states WHERE\
        name = '{}' ORDER BY id ASC".format(state_name)

    # Execute the SQL query
    cursor.execute(query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Iterate over rows and print results
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    connection.close()


if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username>\
            <mysql_password> <db_name> <state_name>\
                ".format(sys.argv[0]))
        sys.exit(1)

    # Extract arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Call filter_states function
    filter_states(mysql_username, mysql_password, db_name, state_name)
