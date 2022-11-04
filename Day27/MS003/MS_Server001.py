
from flask import jsonify, current_app, request

from pyms.flask.app import Microservice


ms = Microservice()
app = ms.create_app()

@app.route("/")
def home():
    app.logger.info("These are my headers: {}".format(request.headers))
    response = app.ms.requests.get("https://jsonplaceholder.typicode.com/photos/3")
    return jsonify({"response": response.json()})

if __name__ == '__main__':
    app.run()