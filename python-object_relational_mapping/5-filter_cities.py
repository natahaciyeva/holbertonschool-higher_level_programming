#!/usr/bin/python3
"""
Lists all cities of a state from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def main():
    if len(sys.argv) != 5:
        return

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=db_name,
        port=3306
    )

    cursor = db.cursor()

    # SQL injection free query using placeholders
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
    """

    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()

    # Extract city names into a list
    city_names = [row[0] for row in rows]

    # Print in required format
    print(", ".join(city_names))

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()

