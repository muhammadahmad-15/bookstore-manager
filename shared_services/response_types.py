from flask import jsonify


def success_response(status_code: int, message: str, data=None):
    response = {
        "status_code": status_code,
        "message": message
    }
    if data is not None:
        response['data'] = data
    return jsonify(response), status_code


def error_response(status_code: int, error: str):
    response = {
        "status_code": status_code,
        "error": error
    }
    return jsonify(response), status_code