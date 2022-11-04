
from flask import jsonify, current_app, request

from pyms.flask.app import Microservice

ms = Microservice()
app = ms.create_app()

@app.route("/")
def index():
    app.logger.info("These are headers: \n{}".format(request.headers))
    response = app.ms.requests.get("http://127.0.0.1:5000/")
    return jsonify({'response': response.json()})

if __name__ == '__main__':
    app.run(port=5001)