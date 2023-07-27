from flask import request, jsonify
from bson import json_util, ObjectId
from models.allModels import venueCollection

import json


def get_all_venues():
    try:
        data = venueCollection.find({})
        serialisedData = json_util.dumps(data)
        response = json.loads(serialisedData)
        return jsonify(response)
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def get_one_venue(venue_id):
    try:
        venue_id = ObjectId(venue_id)
        data = venueCollection.find_one({'_id': venue_id})

        if not data:
            return jsonify({'message': "venue with the given id does not exist."}), 400

        serialised_data = json_util.dumps(data)
        response = json.loads(serialised_data)
        return jsonify(response)
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def add_venue():
    try:
        data = request.get_json()

        is_present = venueCollection.find_one(
            {'name': data['name'], 'city': data['city'], "location": data['location']})

        if is_present:
            return jsonify({'message': "Venue already exists"}), 400

        venueCollection.insert_one(data)
        return jsonify({'message': "Venue data added."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def add_venues():
    try:
        data = request.get_json()

        # Check if data is a list of venues
        if not isinstance(data, list):
            return jsonify({'message': 'Invalid data format. Expected a list of venues.'}), 400

        # Validate each venue in the list before inserting
        for venue in data:
            if not isinstance(venue, dict):
                return jsonify({'message': 'Invalid data format. Each venue should be a dictionary.'}), 400

            # Check if the venue name already exists in the database
            is_present = venueCollection.find_one({'name': venue.get('name')})
            if is_present:
                return jsonify({'message': f"venue '{venue.get('name')}' already exists."}), 400

            # Insert the venue into the database
            venueCollection.insert_one(venue)

        return jsonify({'message': f"{len(data)} venues added to the database."}), 200

    except Exception as e:
        return jsonify({"message": str(e)}), 500


def edit_venue(venue_id):
    try:
        venue_id = ObjectId(venue_id)
        data = request.get_json()

        is_present = venueCollection.find_one({'_id': venue_id})

        if not is_present:
            return jsonify({'message': "venue with the given id does not exist."}), 400

        venueCollection.update_one({"_id": venue_id}, {'$set': data})
        return jsonify({'message': "Edited the venue data successfully."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def delete_venue(venue_id):
    try:
        venue_id = ObjectId(venue_id)

        is_present = venueCollection.find_one({'_id': venue_id})

        if not is_present:
            return jsonify({'message': "Venue with the given id does not exist."}), 400

        venueCollection.delete_one({"_id": venue_id})
        return jsonify({'message': "Venue deleted successfully."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
