from flask import Flask
from flask import make_response
import logging
app = Flask(__name__)

logging.basicConfig(filename="app.log",format="%(asctime)s, %(message)s",level=logging.DEBUG)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status():
    resp = make_response({
        "result": "OK - healthy"
    }, 200)
    app.logger.debug("status endpoint was reached")
    return resp

@app.route("/metrics")
def metrics():
    resp = make_response({
        "data": {
            "UserCount": 140,
            "UserCountActive": 23
        }
    }, 200)
    app.logger.debug("metrics endpoint was reached")
    return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0')
