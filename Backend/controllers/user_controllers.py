from flask import request, jsonify
import bcrypt
import jwt
import datetime
from bson import ObjectId

from models.allModels import user_schema, validate_data, userCollection


def generate_token(id):
    # Define the payload with user-specific data
    payload = {
        'id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expiration time
    }

    # Encode the payload and generate the token

    # EvenTix is the secret_key
    token = jwt.encode(payload, 'EvenTix', algorithm='HS256')
    return token


def user_login():
    data = request.get_json()

    valid = validate_data(data, {"email": str, 'password': str})

    if not valid:
        return jsonify({"message": "Invalid data"}), 400

    email = data['email']
    password = data['password']
    if email == '' or password == '':
        return jsonify({"message": "Fill all the details."}), 400

    # Retrieve the user document from the collection based on the provided user_name
    user_document = userCollection.find_one({'email': email})

    if user_document is None:
        return jsonify({'message': 'Invalid email'}), 401

    # Convert the ObjectId field to a string
    user_document['_id'] = str(user_document['_id'])

    # Verify the password
    hashed_password = user_document['password']

    if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
        # Successful login
        # Generate and return an authentication token
        token = generate_token(user_document['_id'])
        return jsonify({'message': 'Login successful', 'user': user_document, 'token': token}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401


def user_signup():
    try:
        data = request.get_json()

        # Validate data against user schema
        valid = validate_data(
            data, {"email": str, 'password': str, 'name': str})

        if not valid:
            return jsonify({"message": "Invalid data"}), 400

        if data["email"] == "" or data['password'] == "" or data['name'] == "":
            return jsonify({"message": "Enter all the details."}), 400

        # Check if email is unique

        if userCollection.find_one({'email': data['email']}) is not None:
            return jsonify({"message": "Email already exists"}), 409

        # Hash the password
        hashed_password = bcrypt.hashpw(
            data['password'].encode(), bcrypt.gensalt())

        # Insert user data into the collection
        userCollection.insert_one({
            'email': data['email'], 'name': data['name'],
            'password': hashed_password.decode(), 'membership': "", 'bio': "", 'date_of_birth': "", 'age': ''
        })

        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def edit_profile(user_id):
    try:
        user_id = ObjectId(user_id)
        data = request.get_json()
        is_present = userCollection.find_one({"_id": user_id})

        if not is_present:
            return jsonify({'message': "User not found."}), 400

        userCollection.update_one({'_id': user_id}, {'$set': data})

        return jsonify({'message': 'Profile edited successfully'}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def delete_user(user_id):
    user_id = ObjectId(user_id)
    try:
        is_present = userCollection.find_one({"_id": user_id})

        if not is_present:
            return jsonify({'message': "User not found."}), 400

        userCollection.delete_one({"_id": user_id})
        return jsonify({'message': 'User deleted successfully'}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 500
