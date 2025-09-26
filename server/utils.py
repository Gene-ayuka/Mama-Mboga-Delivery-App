from flask import jsonify

def success_response(message, data=None, status_code=200):
    """Standard success response format"""
    response = {"success": True, "message": message}
    if data is not None:
        response["data"] = data
    return jsonify(response), status_code

def error_response(message, status_code=400):
    """Standard error response format"""
    return jsonify({"success": False, "message": message}), status_code