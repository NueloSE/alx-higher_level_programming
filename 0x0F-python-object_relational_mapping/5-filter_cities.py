#!/usr/bin/python3

"""
 a script that takes in the name of a state as an argument and lists all
 cities of that state, using the database hbtn_0e_4_usa

Your script should take 4 arguments: mysql username, mysql password, database
name and state name (SQL injection free!)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
The results must be displayed as they are in the example below
Your code should not be executed when imported
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )
    cur = db.cursor()
    querry = "SELECT c.name FROM cities c JOIN states s ON c.state_id = s.id \
        WHERE s.name = %s"
    cur.execute(querry, (argv[4],))
    querry_rows = cur.fetchall()
    state_names = ', '.join(row[0] for row in querry_rows)
    print(state_names)
    cur.close()
    db.close()
