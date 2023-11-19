import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySQLiteDBConnection import Connect

connection = Connect("tests/database.db")

print(connection)

connection.connect()

print(connection)

connection.close()

print(connection)
