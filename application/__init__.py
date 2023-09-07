from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create the Flask application
app = Flask(__name__)

# Configure the Flask app with a SQLite database URI
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:\\\Users\xmika\Codebusters\Codebusters' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mock_database.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable tracking modifications (optional)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a secret key

# Create the SQLAlchemy database object
db = SQLAlchemy(app)

# Import your routes and models
from application import routes, models

