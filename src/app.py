from flask import Flask, request, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Login post"
    else:
        return "Login form"


"""
To build a URL to a specific function, use the url_for() function. It accepts the name of the function as its 
first argument and any number of keyword arguments, each corresponding to a variable part of the URL rule. Unknown 
variable parts are appended to the URL as query parameters. 
"""

url_for('static', filename='style.css')

"""
Just make sure not to forget to set the enctype="multipart/form-data" attribute on your HTML form, otherwise the 
browser will not transmit your files at all. 
"""


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('uploads/' + secure_filename(f.filename))


if __name__ == '__main__':
    app.run()
