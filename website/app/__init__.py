# Dependency: pip install flask requests
from flask import Flask, request
# Define Flask webserver
app = Flask(__name__)

from app import routes, laundry_viewer
