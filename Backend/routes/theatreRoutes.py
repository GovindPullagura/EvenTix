from flask import Blueprint
from controllers.theatre_controllers import get_all_theatres, add_theatre, add_theatres, edit_theatre, delete_theatre

theatre_router = Blueprint('theatre', __name__)

theatre_router.route('/', methods=['GET'])(get_all_theatres)
theatre_router.route('/addTheatre', methods=["POST"])(add_theatre)
theatre_router.route('/addTheatres', methods=["POST"])(add_theatres)
theatre_router.route('/deleteTheatre/<theatre_id>',
                     methods=["DELETE"])(delete_theatre)
theatre_router.route('/editTheatre/<theatre_id>',
                     methods=["PATCH"])(edit_theatre)
