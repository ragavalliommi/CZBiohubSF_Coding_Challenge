import sqlite3

# Connect to database
connection = sqlite3.connect('fibonacci.db')

# Create a cursor
c = connection.cursor()

# Create a table
c.execute("""CREATE TABLE fibonacciNumbers (
        number integer,
        sequence text
    )""")

# Commit command
connection.commit()

# Close connection
connection.close()