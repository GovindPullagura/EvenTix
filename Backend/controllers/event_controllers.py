from flask import request, jsonify
from bson import json_util, ObjectId
from models.allModels import eventCollection, venueCollection

import json


def get_all_events():
    try:
        data = eventCollection.find({})
        serialisedData = json_util.dumps(data)
        response = json.loads(serialisedData)
        return jsonify(response)
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def get_one_event(event_id):
    try:
        event_id = ObjectId(event_id)
        data = eventCollection.find_one({'_id': event_id})

        if not data:
            return jsonify({'message': "Event with the given id does not exist."}), 400

        venue = venueCollection.find_one({"_id": ObjectId(data['venue_id'])})
        data["venue"] = venue

        serialised_data = json_util.dumps(data)
        response = json.loads(serialised_data)
        return jsonify(response)
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def add_event():
    try:
        data = request.get_json()

        is_present = eventCollection.find_one(
            {'name': data['name'], 'language': data['language']})

        if is_present:
            return jsonify({'message': "Event already exists"}), 400

        eventCollection.insert_one(data)
        return jsonify({'message': "Event data added."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def edit_event(event_id):
    try:
        event_id = ObjectId(event_id)
        data = request.get_json()

        is_present = eventCollection.find_one({'_id': event_id})

        if not is_present:
            return jsonify({'message': "Event with the given id does not exist."}), 400

        eventCollection.update_one({"_id": event_id}, {'$set': data})
        return jsonify({'message': "Edited the event data successfully."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def delete_event(event_id):
    try:
        event_id = ObjectId(event_id)

        is_present = eventCollection.find_one({'_id': event_id})

        if not is_present:
            return jsonify({'message': "Event with the given id does not exist."}), 400

        eventCollection.delete_one({"_id": event_id})
        return jsonify({'message': "Event deleted successfully."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def add_events():
    try:
        data = request.get_json()

        # Check if data is a list of events
        if not isinstance(data, list):
            return jsonify({'message': 'Invalid data format. Expected a list of events.'}), 400

        # Validate each event in the list before inserting
        for event in data:
            if not isinstance(event, dict):
                return jsonify({'message': 'Invalid data format. Each event should be a dictionary.'}), 400

            # Check if the event title already exists in the database
            is_present = eventCollection.find_one(
                {'name': event.get('name')})
            if is_present:
                return jsonify({'message': f"event '{event.get('name')}' already exists."}), 400

            # Insert the event into the database
            eventCollection.insert_one(event)

        return jsonify({'message': f"{len(data)} events added to the database."}), 200

    except Exception as e:
        return jsonify({"message": str(e)}), 500
