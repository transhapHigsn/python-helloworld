import logging
import time

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    now = time.time()
    app.logger.info(f"{now}, / endpoint was reached")
    return "Hello World!"

@app.route("/status")
def status():
    now = time.time()
    app.logger.info(f"{now}, /status endpoint was reached")
    return jsonify({"result": "Ok - healthy"}), 200

@app.route("/metrics")
def metrics():
    now = time.time()
    app.logger.info(f"{now}, /metrics endpoint was reached")
    return jsonify({
        "status": "success",
        "code": 0,
        "data": {
            "UserCount": 140, 
            "UserCountActive": 23
        }
    }), 200

if __name__ == "__main__":
    log = logging.basicConfig(filename="app.log", level=logging.DEBUG)
    app.run(host='0.0.0.0', port=5000, debug=True)
