# Import Flask
from flask import Flask

# Create Flask instance
app = Flask(__name__)

# Create Flask routes
@app.route('/')
def hello_world():
    return 'Hello world'