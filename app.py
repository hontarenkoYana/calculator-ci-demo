from calculator import Calculator
from flask import Flask, request, render_template
import logging
app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/addition', methods=["POST"])
def add():
    first_term = int(request.form['first_term'])
    second_term = int(request.form['second_term'])
    return render_template("index.html", result=Calculator().add(first_term, second_term))

@app.route('/substraction', methods=["POST"])
def substraction():
    first_term = int(request.form['first_term'])
    second_term = int(request.form['second_term'])
    return render_template("index.html", result=Calculator().subtract(first_term, second_term))

@app.route('/multiplication', methods=["POST"])
def multiplication():
    first_term = int(request.form['first_term'])
    second_term = int(request.form['second_term'])
    return render_template("index.html", result=Calculator().multiplication(first_term, second_term))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)     # open for everyone
