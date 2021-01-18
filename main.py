from flask import Flask
app = Flask (__name__)

try:


@app.route('/user', methods =['POST'])
def create_user():
    return "passt"


if __name__ == '__main__':
    app.run(port=42, debug=True)