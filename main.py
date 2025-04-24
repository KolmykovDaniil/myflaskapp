from flask import Flask
import logging

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
app.logger.info("Starting Flask application")

@app.route('/')
def hello_world():
    app.logger.info("Received request to /")
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(port=5000)