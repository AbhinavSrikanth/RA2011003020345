from flask import Flask, request, jsonify
import requests

app = Flask(__name__)



#prime numbers
@app.route('/primes', methods=['GET'])
def get_prime_numbers():
    url = "http://20.244.56.144/numbers/primes"
    response = requests.get(url, timeout=0.5)
    if response.status_code == 200:
        data = response.json()
        prime_numbers = data.get('numbers', [])
        return jsonify(numbers=prime_numbers)
    return jsonify(error="Error fetching prime numbers"), 500


#fibonaccinumbers
@app.route('/fibo', methods=['GET'])
def get_fibonacci_numbers():
    url = "http://20.244.56.144/numbers/fibo"
    response = requests.get(url, timeout=0.5)
    if response.status_code == 200:
        data = response.json()
        fibonacci_numbers = data.get('numbers', [])
        return jsonify(numbers=fibonacci_numbers)
    return jsonify(error="Error fetching Fibonacci numbers"), 500

#odd numbers
@app.route('/odd', methods=['GET'])
def get_odd_numbers():
    url = "http://20.244.56.144/numbers/odd"
    response = requests.get(url, timeout=0.5)
    if response.status_code == 200:
        data = response.json()
        odd_numbers = data.get('numbers', [])
        return jsonify(numbers=odd_numbers)
    return jsonify(error="Error fetching odd numbers"), 500

#random numbers
@app.route('/rand', methods=['GET'])
def get_random_numbers():
    url = "http://20.244.56.144/numbers/rand"
    response = requests.get(url, timeout=0.5)
    if response.status_code == 200:
        data = response.json()
        random_numbers = data.get('numbers', [])
        return jsonify(numbers=random_numbers)
    return jsonify(error="Error fetching random numbers"), 500


if __name__ == '__main__':
    app.run(debug=True)
