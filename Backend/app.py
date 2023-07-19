import os
from flask import Flask
from flask_cors import CORS
from routes.userRoutes import user_router


# Create the Flask application
app = Flask(__name__)

# Configure CORS to allow cross-origin requests
CORS(app)


@app.route("/")
def home():
    return 'Welcome to EvenTix!'


app.register_blueprint(user_router, url_prefix='/users')


# app.py

if __name__ == '__main__':
    app.run(debug=True)
