from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/home', methods = ['GET'])
def home():
    sequence = "Hello World"
    
    # if check_n_in_db(n):
    #     sequence = get_fibonacci_from_db(n)
    # else:
    #     sequence = compute_fibonacci(n)
    #     save_fibonacci_to_db(n, sequence)
    
    return sequence


# def check_n_in_db(n):
#     return True

# def get_fibonacci_from_db(n):
#     return

# def compute_fibonacci(n):
#     return

# def save_fibonacci_to_db(n, sequence):
#     return

if __name__ == "__main__":
    app.run(debug=True)