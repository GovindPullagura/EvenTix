from flask import request, jsonify
from bson import json_util, ObjectId
from models.allModels import bookingCollection

import json


def get_all_bookings():
    try:
        data = bookingCollection.find({})
        serialisedData = json_util.dumps(data)
        response = json.loads(serialisedData)
        return jsonify(response)
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def get_user_bookings(user_id):
    try:
        data = bookingCollection.find({'user_id': user_id})
        serialisedData = json_util.dumps(data)
        response = json.loads(serialisedData)
        return jsonify(response)
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def book_event():
    try:
        data = request.get_json()
        bookingCollection.insert_one(data)
        return jsonify({'message': "Booking successful."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def delete_booking(booking_id):
    try:
        booking_id = ObjectId(booking_id)

        is_present = bookingCollection.find_one({'_id': booking_id})

        if not is_present:
            return jsonify({'message': "booking with the given id does not exist."}), 400

        bookingCollection.delete_one({"_id": booking_id})
        return jsonify({'message': "booking deleted successfully."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
