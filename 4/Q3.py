# 3. Implement error status code to the abort() function for a bad request, so it raises
# a Bad Request Error and forbidden error using flask.
from flask import Flask, abort, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h2>Flask Error Testing</h2>

    <form action="/test" method="post">
        <label>Enter your age:</label>
        <input type="number" name="age" required>
        <button type="submit">Submit</button>
    </form>

    <br>
    <a href="/forbidden">Test Forbidden Error</a>
    '''

@app.route('/test', methods=['POST'])
def test():
    age = int(request.form['age'])

    if age < 18:
        abort(400, description="Bad Request: Age must be 18 or above.")

    return "<h3>Success! Your age is valid.</h3>"

@app.route('/forbidden')
def forbidden():
    abort(403, description="Forbidden: You are not allowed to access this page.")

if __name__ == '__main__':
    app.run(debug=True)