from flask import Flask, jsonify, make_response

app = Flask(__name__)


# Not found
@app.errorhandler(404)
def handle_resource_not_found(_unused):
    return make_response(jsonify({'error': 'Resource not found'}), 404)


# Request timeout
@app.errorhandler(408)
def handle_overloaded_server(_unused):
    return make_response(jsonify({'error': 'The server is overloaded. Try later.'}), 408)


# Internal server error
@app.errorhandler(500)
def handler_server_internal_error(_unused):
    return make_response(jsonify({'error': 'The server encountered an internal '
                                           'error and was unable to complete your request.'}), 500)
