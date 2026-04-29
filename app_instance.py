from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')
CORS(app, resources={r"/*Z": {"origins": "*"}})