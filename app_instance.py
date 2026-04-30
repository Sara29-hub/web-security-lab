from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')
CORS(app, resources={r"/*Z": {"origins": "*"}})

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=[]
)