from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Add your SQLAlchemy configuration here
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://hbnb_dev:your_password@localhost/your_database_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import your routes here
from web_flask import routes
