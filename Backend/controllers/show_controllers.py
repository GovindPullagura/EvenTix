from flask import request, jsonify
from bson import json_util, ObjectId
from models.allModels import show_schema, showCollection, movieCollection, theatreCollection
import json


def get_all_shows():
    try:
        data = showCollection.find()
        serialised_data = json_util.dumps(data)
        response = json.loads(serialised_data)
        return jsonify(response)
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def shows_and_theatres(movie_id):
    try:
        mov_id = ObjectId(movie_id)
        movie = movieCollection.find_one({"_id": mov_id})

        if not movie:
            return jsonify({'message': "No movie found with the given ID."})

        data = list(showCollection.find({'movie_id': movie_id}))
        if not data:
            return jsonify({'message': "No shows available for the movie."})

        for show in data:
            show["movie"] = movie
            theatre = theatreCollection.find_one(
                {"_id": ObjectId(show["theatre_id"])})
            show['theatre'] = theatre

        serialised_data = json_util.dumps(data)
        response = json.loads(serialised_data)
        return jsonify(response)
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def add_show():
    try:
        data = request.get_json()

        is_present = showCollection.find_one(
            {'date': data['date'], 'theatre_id': data['theatre_id'], 'screen': data['screen'], 'start_time': data['start_time']})

        if is_present:
            return jsonify({'message': "Slot blocked for a show."}), 400

        showCollection.insert_one(data)
        return jsonify({'message': "Show data added."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def add_shows():
    try:
        data = request.get_json()

        # Check if data is a list of shows
        if not isinstance(data, list):
            return jsonify({'message': 'Invalid data format. Expected a list of shows.'}), 400

        # Validate each show in the list before inserting
        for show in data:
            if not isinstance(show, dict):
                return jsonify({'message': 'Invalid data format. Each show should be a dictionary.'}), 400

            # Check if the show name already exists in the database
            is_present = showCollection.find_one(
                {'date': show.get('date'), 'theatre_id': show.get('theatre_id'), 'screen': show.get('screen'), 'start_time': show.get('start_time')})
            if is_present:
                return jsonify({'message': "show already exists."}), 400

            # Insert the show into the database
            showCollection.insert_one(show)

        return jsonify({'message': f"{len(data)} shows added to the database."}), 200

    except Exception as e:
        return jsonify({"message": str(e)}), 500


def edit_show(show_id):
    try:
        show_id = ObjectId(show_id)
        data = request.get_json()

        is_present = showCollection.find_one({'_id': show_id})

        if not is_present:
            return jsonify({'message': "show with the given id does not exist."}), 400

        showCollection.update_one({"_id": show_id}, {'$set': data})
        return jsonify({'message': "Edited the show data successfully."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def delete_show(show_id):
    try:
        show_id = ObjectId(show_id)

        is_present = showCollection.find_one({'_id': show_id})

        if not is_present:
            return jsonify({'message': "show with the given id does not exist."}), 400

        showCollection.delete_one({"_id": show_id})
        return jsonify({'message': "show deleted successfully."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
