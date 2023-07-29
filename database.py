import sqlite3

# Connect to database
connection = sqlite3.connect('fibonacci.db')

# Create a cursor
c = connection.cursor()

# Create a table
c.execute("""CREATE TABLE IF NOT EXISTS fibonacciNumbers (
                    number INTEGER PRIMARY KEY,
                    sequence TEXT
        )""")

# Commit command
connection.commit()

# Close connection
connection.close()