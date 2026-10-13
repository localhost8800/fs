# 1. Write a program for abort() function in flask with the error code for
# unauthorized access in case of any random password entered by the user.
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'admin123':
            return '''
                <h2>Login Successful!</h2>
                <p>Welcome, admin!</p>
            '''
        else:
            abort(401)

    return '''
        <html>
        <head>
            <title>Login Page</title>
        </head>
        <body>
            <h2>Login Form</h2>

            <form method="POST">
                Username:
                <input type="text" name="username" required>
                <br><br>

                Password:
                <input type="password" name="password" required>
                <br><br>

                <button type="submit">Login</button>
            </form>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)