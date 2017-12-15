from flask import Flask, render_template, Blueprint, abort
from blueprint import simple_page
app = Flask(__name__)
app.register_blueprint(simple_page)


# @app.route("/")
# def index():
#         return "Hello hakjoon with Flask!!"

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=False)
