from flask import Blueprint
from controllers.movie_controllers import get_all_movies, get_one_movie, add_movie, edit_movie, delete_movie,  add_movies


movie_router = Blueprint('movie', __name__)

movie_router.route('/', methods=['GET'])(get_all_movies)
movie_router.route('/<movie_id>', methods=['GET'])(get_one_movie)
movie_router.route('/addMovie', methods=["POST"])(add_movie)
movie_router.route('/addMovies', methods=["POST"])(add_movies)
movie_router.route('/editMovie/<movie_id>', methods=['PATCH'])(edit_movie)
movie_router.route('/deleteMovie/<movie_id>', methods=['DELETE'])(delete_movie)
