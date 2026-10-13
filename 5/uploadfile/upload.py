# 1. Create an application using flask to upload a file from the local file system to
# the server and also display a success message to the user with the name of the uploaded file.
from flask import Flask, render_template, request
import os

app = Flask(__name__)

os.makedirs('uploads', exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']

        if file.filename == '':
            return "No file selected"

        file.save(os.path.join('uploads', file.filename))

        return f"File {file.filename} uploaded successfully!"

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)