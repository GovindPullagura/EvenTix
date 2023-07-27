from flask import request, jsonify
from bson import ObjectId, json_util
from models.allModels import theatre_schema, theatreCollection
import json


def get_all_theatres():
    try:
        data = theatreCollection.find()
        serialised_data = json_util.dumps(data)
        response = json.loads(serialised_data)
        return jsonify(response)
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def add_theatre():
    try:
        data = request.get_json()

        is_present = theatreCollection.find_one(
            {'name': data['name'], 'location': data['location'], 'city': data['city']})

        if is_present:
            return jsonify({'message': "Theatre data already exists"}), 400

        theatreCollection.insert_one(data)
        return jsonify({'message': "Theatre data added."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def add_theatres():
    try:
        data = request.get_json()

        # Check if data is a list of theatres
        if not isinstance(data, list):
            return jsonify({'message': 'Invalid data format. Expected a list of theatres.'}), 400

        # Validate each theatre in the list before inserting
        for theatre in data:
            if not isinstance(theatre, dict):
                return jsonify({'message': 'Invalid data format. Each theatre should be a dictionary.'}), 400

            # Check if the theatre name already exists in the database
            is_present = theatreCollection.find_one(
                {'name': theatre.get('name')})
            if is_present:
                return jsonify({'message': f"theatre '{theatre.get('name')}' already exists."}), 400

            # Insert the theatre into the database
            theatreCollection.insert_one(theatre)

        return jsonify({'message': f"{len(data)} theatres added to the database."}), 200

    except Exception as e:
        return jsonify({"message": str(e)}), 500


def edit_theatre(theatre_id):
    try:
        theatre_id = ObjectId(theatre_id)
        data = request.get_json()

        is_present = theatreCollection.find_one({'_id': theatre_id})

        if not is_present:
            return jsonify({'message': "theatre with the given id does not exist."}), 400

        theatreCollection.update_one({"_id": theatre_id}, {'$set': data})
        return jsonify({'message': "Edited the theatre data successfully."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def delete_theatre(theatre_id):
    try:
        theatre_id = ObjectId(theatre_id)

        is_present = theatreCollection.find_one({'_id': theatre_id})

        if not is_present:
            return jsonify({'message': "theatre with the given id does not exist."}), 400

        theatreCollection.delete_one({"_id": theatre_id})
        return jsonify({'message': "theatre deleted successfully."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
