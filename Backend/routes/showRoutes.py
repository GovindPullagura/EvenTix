from flask import Blueprint
from controllers.show_controllers import get_all_shows, add_show, add_shows, delete_show, shows_and_theatres, edit_show

show_router = Blueprint('show', __name__)

show_router.route('/', methods=['GET'])(get_all_shows)
show_router.route('/<movie_id>', methods=['GET'])(shows_and_theatres)
show_router.route('/addShow', methods=["POST"])(add_show)
show_router.route('/addShows', methods=["POST"])(add_shows)
show_router.route('/deleteShow/<show_id>', methods=["DELETE"])(delete_show)
show_router.route('/editShow/<show_id>', methods=["PATCH"])(edit_show)
