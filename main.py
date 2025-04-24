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
    app.logger.info("Running on http://0.0.0.0:5000")
    app.run(host='0.0.0.0', port=5000)