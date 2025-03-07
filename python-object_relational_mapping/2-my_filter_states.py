#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL connection parameters from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor object to execute SQL queries
        cursor = db.cursor()

        # Create the SQL query using format to include user input
        query = "SELECT * FROM states WHERE name = '{}' \
            ORDER BY id ASC".format(state_name)

        # Execute the query
        cursor.execute(query)

        # Fetch all the rows that match the query
        states = cursor.fetchall()

        # Display the results
        for state in states:
            print(state)

        # Close the cursor and database connection
        cursor.close()
        db.close()
