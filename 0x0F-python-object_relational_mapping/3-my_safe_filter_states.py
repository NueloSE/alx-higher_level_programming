#!/usr/bin/python3
"""
Once again, write a script that takes in arguments and
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument. But this time,
write one that is safe from MySQL injections!

Your script should take 4 arguments: mysql username,
mysql password, database name and state name searched
(safe from MySQL injection)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
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
    querry = "SELECT * FROM states WHERE name = BINARY %s ORDER BY id ASC"
    cur.execute(querry, (argv[4],))
    querry_row = cur.fetchall()
    for row in querry_row:
        print(row)
    cur.close()
    db.close()
