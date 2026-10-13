# 2. Design flask application to print the table of a number specified in the URL.if
# url is http://localhost:5000/table/10 then it will print the table of 10 on the browser's window.
from flask import Flask

app = Flask(__name__)

@app.route('/table/<int:num>')
def table(num):
    result = f"<h2>Table of {num}</h2>"
    for i in range(1, 11):
        result += f"{num} x {i} = {num * i}<br>"
    return result

if __name__ == '__main__':
    app.run(debug=True)