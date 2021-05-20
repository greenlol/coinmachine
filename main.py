import flask
from flask import request, jsonify
import requests

app = flask.Flask(__name__)
app.config["DEBUG"] = True

baseurl = 'https://a.4cdn.org/'

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404




@app.route('/test', methods=['GET'])
def test():
    """
    test call
    """
    resource = 'boards.json'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url=baseurl+resource,
                            headers=headers,
                            verify=True)
    return response.json()


app.run(host='0.0.0.0')
