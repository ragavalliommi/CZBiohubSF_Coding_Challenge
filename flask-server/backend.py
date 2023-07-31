from flask import Flask, request
import sqlite3
import os

db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'fibonacci.db')
print(db_path)
app = Flask(__name__)

@app.route('/home', methods = ['GET'])
def home():
    n = int(request.args.get('n'))
    sequence = []
    sequenceTuple = get_fibonacci_from_db(n)

    if sequenceTuple is not None:
        sequence = list(map(int, sequenceTuple[0].split(', ')))
    else:
        sequence = compute_fibonacci(n)
        save_fibonacci_to_db(n, sequence)

    return sequence

def get_fibonacci_from_db(n):
    connection = sqlite3.connect(db_path)
    c = connection.cursor()
    c.execute("SELECT sequence FROM fibonacciNumbers WHERE number = ?", (n,))
    result = c.fetchone()
    connection.close()
    return result

def compute_fibonacci(n):
    result = [0, 1]
    for i in range(2, n):
        result.append(result[i-1] + result[i-2])
    return result

def save_fibonacci_to_db(n, sequence):
    connection = sqlite3.connect(db_path)
    c = connection.cursor()
    sequenceText = ', '.join(map(str,sequence))
    c.execute("""INSERT INTO fibonacciNumbers (number, sequence)
                VALUES (?, ?) 
    """, (n, sequenceText))
    connection.commit()
    connection.close()
    return

if __name__ == "__main__":
    app.run(debug=True)