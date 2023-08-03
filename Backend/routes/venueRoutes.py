from flask import Blueprint
from controllers.venue_controllers import get_all_venues, get_one_venue, add_venue, edit_venue, add_venues, delete_venue


venue_router = Blueprint('venue', __name__)

venue_router.route('/', methods=['GET'])(get_all_venues)
venue_router.route('/<venue_id>', methods=['GET'])(get_one_venue)
venue_router.route('/addVenue', methods=["POST"])(add_venue)
venue_router.route('/addVenues', methods=["POST"])(add_venues)
venue_router.route('/editVenue/<venue_id>', methods=['PATCH'])(edit_venue)
venue_router.route('/deleteVenue/<venue_id>', methods=['DELETE'])(delete_venue)
