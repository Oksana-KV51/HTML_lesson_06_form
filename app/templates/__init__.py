from flask import Flask
from .app import app
#создаёт экземпляр класса Flask (переменную app)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
from app import routes

