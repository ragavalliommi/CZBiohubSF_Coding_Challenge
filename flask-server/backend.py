from flask import Flask, request
import sqlite3
import os

db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'fibonacci.db')
print(db_path)
app = Flask(__name__)

@app.route('/home', methods = ['GET'])
def home():
    n = int(request.args.get('n'))
    sequence = ""
    
    if check_n_in_db(n):
        #sequence = get_fibonacci_from_db(n)
        sequence = "It is there in DB"
    else:
        # sequence = compute_fibonacci(n)
        # save_fibonacci_to_db(n, sequence)
        sequence = "It is not there in DB"
    
    return sequence


def check_n_in_db(n):
    connection = sqlite3.connect(db_path)
    c = connection.cursor()
    c.execute("SELECT * FROM fibonacciNumbers WHERE number = ?",(n,))
    result = c.fetchone()
    connection.close()
    return result is not None

def get_fibonacci_from_db(n):
    return

def compute_fibonacci(n):
    return

def save_fibonacci_to_db(n, sequence):
    return

if __name__ == "__main__":
    app.run(debug=True)