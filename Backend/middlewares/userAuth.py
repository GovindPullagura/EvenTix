from flask import request, jsonify
import jwt

# Middleware for profile access control


def check_profile_access():
    # List of routes to exclude from the middleware
    excluded_routes = ['/users/login', '/users/signup']

    # Get the request path to check if it matches any of the excluded routes
    request_path = request.path

    # Check if the request path is in the list of excluded routes
    if request_path in excluded_routes:
        return

    # Get the JWT token from the Authorization header
    token = request.headers.get('Authorization')

    if token:
        try:
            # Remove the "Bearer " prefix from the token (if present)
            if token.startswith('Bearer '):
                token = token.split(' ')[1]

            # Decode the token to get the user's identity (e.g., email)
            payload = jwt.decode(token, 'EvenTix', algorithms=['HS256'])
            id = payload.get('id')

            # Assuming you have a route parameter named 'user_id' representing the user's ID
            user_id = request.view_args.get('user_id')
            user_id_str = str(user_id)  # Convert user_id to string

            # Check if the user's identity matches the profile being accessed
            if user_id_str and user_id_str == id:
                # Allow access to edit or delete the profile
                return

            # If the user's identity does not match, deny access with a 403 Forbidden status code
            return jsonify({"message": "Access forbidden. You can only edit/delete your own profile."}), 403

        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired. Please log in again."}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token. Please log in again."}), 401

    # If no token is provided and the route is not excluded, return a 401 Unauthorized status code
    return jsonify({"message": "Authorization token is missing. Please log in."}), 401
