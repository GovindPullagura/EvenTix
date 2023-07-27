from flask import request, jsonify
from bson import json_util, ObjectId
from models.allModels import movieCollection, movieCollection
import json


def get_all_movies():
    try:
        # Get the filter parameters from the request
        versions = request.args.getlist('version')
        languages = request.args.getlist('language')
        genre = request.args.get('genre')

        # Create a filter query based on the provided parameters
        filter_query = {}
        if versions:
            filter_query['versions'] = {'$in': versions}
        if languages:
            filter_query['languages'] = {'$in': languages}
        if genre:
            filter_query['genre'] = genre

        # Create the aggregation pipeline for sorting and filtering
        pipeline = [
            # Apply the filter query
            {'$match': filter_query},
            # Sort the data based on the release_date in descending order
            {'$sort': {'release_date': -1}}
        ]

        # Fetch the data using the aggregation pipeline
        data = movieCollection.aggregate(pipeline)

        # Serialize the data and convert it to a list of dictionaries
        serialisedData = json_util.dumps(data)
        response = json.loads(serialisedData)

        return jsonify(response)
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def get_one_movie(movie_id):
    try:
        movie_id = ObjectId(movie_id)
        data = movieCollection.find_one({'_id': movie_id})

        if not data:
            return jsonify({'message': "Movie with the given id does not exist."}), 400

        serialised_data = json_util.dumps(data)
        response = json.loads(serialised_data)
        return jsonify(response)
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def add_movie():
    try:
        data = request.get_json()

        is_present = movieCollection.find_one({'title': data['title']})

        if is_present:
            return jsonify({'message': "Movie already exists"}), 400

        movieCollection.insert_one(data)
        return jsonify({'message': "Movie data added."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def add_movies():
    try:
        data = request.get_json()

        # Check if data is a list of movies
        if not isinstance(data, list):
            return jsonify({'message': 'Invalid data format. Expected a list of movies.'}), 400

        # Validate each movie in the list before inserting
        for movie in data:
            if not isinstance(movie, dict):
                return jsonify({'message': 'Invalid data format. Each movie should be a dictionary.'}), 400

            # Check if the movie title already exists in the database
            is_present = movieCollection.find_one(
                {'title': movie.get('title')})
            if is_present:
                return jsonify({'message': f"Movie '{movie.get('title')}' already exists."}), 400

            # Insert the movie into the database
            movieCollection.insert_one(movie)

        return jsonify({'message': f"{len(data)} movies added to the database."}), 200

    except Exception as e:
        return jsonify({"message": str(e)}), 500


def edit_movie(movie_id):
    try:
        movie_id = ObjectId(movie_id)
        data = request.get_json()

        is_present = movieCollection.find_one({'_id': movie_id})

        if not is_present:
            return jsonify({'message': "Movie with the given id does not exist."}), 400

        movieCollection.update_one({"_id": movie_id}, {'$set': data})
        return jsonify({'message': "Edited the movie data successfully."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def delete_movie(movie_id):
    try:
        movie_id = ObjectId(movie_id)

        is_present = movieCollection.find_one({'_id': movie_id})

        if not is_present:
            return jsonify({'message': "Movie with the given id does not exist."}), 400

        movieCollection.delete_one({"_id": movie_id})
        return jsonify({'message': "Movie deleted successfully."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
