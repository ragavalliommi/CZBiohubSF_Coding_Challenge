import sqlite3

# Connect to database
connection = sqlite3.connect('fibonacci.db')

# Create a cursor
c = connection.cursor()

table_name = 'fibonacciNumbers'

# chcek if fibonacciNumbers table exists in schema
check_table_query = f"SELECT name FROM sqlite_master WHERE type = 'table' AND name='{table_name}';"

c.execute(check_table_query)

table_exists = c.fetchone()

# Create table and insert starter row if table does not exist
if not table_exists:
        
        # Create a table
        c.execute("""CREATE TABLE fibonacciNumbers (
                    number INTEGER PRIMARY KEY,
                    sequence TEXT
        )""")

        # Insert first 2 numbers (1 and 2) and their respective Fibonacci sequences
        starterRows = [(1, "0"),
                       (2, "0, 1")]

        c.executemany("""INSERT INTO fibonacciNumbers (number, sequence) VALUES (?, ?)""", starterRows)

        # Commit command
        connection.commit()


# Close connection
connection.close()