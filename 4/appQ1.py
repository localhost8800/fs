# 1. Design simple web application using Flask to display the message
# "Welcome to Nowrosjee Wadia College Pune".

from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to Nowrosjee Wadia College Pune"

if __name__ == '__main__':
    app.run(debug=True)