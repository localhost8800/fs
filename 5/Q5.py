
from flask import Flask, request, make_response, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'admin123':
            response = make_response(redirect('/home'))
            response.set_cookie('username', username)
            return response
        else:
            return "Invalid username or password!"

    return '''
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
    '''

@app.route('/home')
def home():
    username = request.cookies.get('username')

    if username:
        return f'''
            <h2>Welcome, {username}!</h2>
            <p>Login successful using cookies.</p>
            <a href="/logout">Logout</a>
        '''

    return redirect('/')

@app.route('/logout')
def logout():
    response = make_response(redirect('/'))
    response.delete_cookie('username')
    return response

if __name__ == '__main__':
    app.run(debug=True)