from flask import Flask, request
from flask_cors import CORS

import sqlite3
import os, json

db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'fibonacci.db')

app = Flask(__name__)
CORS(app)

@app.route('/home', methods = ['GET'])
def home():

    try:
        # Get the 'n' value from the request parameters
        n = int(request.args.get('n'))

        sequence = []
        sequenceTuple = get_fibonacci_from_db(n)

        if sequenceTuple is not None:
            # If the Fibonacci sequence is found in the database, convert it to a list
            sequence = list(map(int, sequenceTuple[0].split(', ')))
        else:
            # If the Fibonacci sequence is not found, compute it and save it to the database
            sequence = compute_fibonacci(n)
            save_fibonacci_to_db(n, sequence)
        
        # Return the Fibonacci sequence as a JSON response
        return json.dumps(sequence)
    
    except ValueError as ve:
        # Handle ValueError and return a JSON error response
        return json.dumps({"error": str(ve)}), 400

    except sqlite3.Error as sqle:
        # Handle database-related errors and return a JSON error response
        return json.dumps({"error": "Database error: " + str(sqle)}), 500

    except Exception as e:
        # Handle other unexpected errors and return a JSON error response
        return json.dumps({"error": "An unexpected error occurred: " + str(e)}), 500


def get_fibonacci_from_db(n):
    try:
        # Connect to the database and retrieve the Fibonacci sequence for the given 'n'
        connection = sqlite3.connect(db_path)
        c = connection.cursor()
        c.execute("SELECT sequence FROM fibonacciNumbers WHERE number = ?", (n,))
        result = c.fetchone()
        connection.close()
        return result
    
    except sqlite3.Error as sqle:
        # Handle database-related errors and raise the exception 
        # to be caught in the calling function
        raise sqle

def compute_fibonacci(n):
    try:
        # Compute the Fibonacci sequence up to the given 'n'
        result = [0, 1]
        for i in range(2, n):
            result.append(result[i-1] + result[i-2])
        return result
    
    except Exception as e:
        # Handle other unexpected errors and raise the exception 
        # to be caught in the calling function
        raise e

def save_fibonacci_to_db(n, sequence):
    try:
        # Save the Fibonacci sequence to the database for the given 'n'
        connection = sqlite3.connect(db_path)
        c = connection.cursor()
        sequenceText = ', '.join(map(str,sequence))
        c.execute("""INSERT INTO fibonacciNumbers (number, sequence)
                    VALUES (?, ?) 
        """, (n, sequenceText))
        connection.commit()
        connection.close()
        
    except sqlite3.Error as sqle:
        # Handle database-related errors and raise the exception
        # to be caught in the calling function
        raise sqle

if __name__ == "__main__":
    app.run(debug=True)