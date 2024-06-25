from flask import Flask, request, Response
from flask_cors import CORS, cross_origin
import logging
import json
from algo_f_baby import rap

app = Flask(__name__)
# Security stuff
CORS(app)
app.logger.setLevel(logging.INFO)

# This is where we receive the post request from the webpage
@app.route("/test", methods=["POST"])
@cross_origin()
def post_example():
    """POST in server"""
    # Put this in a try-catch -- I'm being lazy
    # request.data is the the "body" we saw in the html
    # Here we interpret it as a JSON dictionary
    data = json.loads(request.data)
    # data["very_cool_data"] extracts the thing we want from the JSON we got from request.data
    app.logger.info("Got this very cool data: {}".format(data["very_cool_data"]))

    generated_rap = rap(data["very_cool_data"])
    rap_dictonary = {'data': generated_rap}

    return rap_dictonary, 200


# Security stuff
@app.before_request
def handle_preflight():
    if request.method == "OPTIONS":
        res = Response()
        res.headers['X-Content-Type-Options'] = '*'
        return res

if __name__ == '__main__':
   app.run()