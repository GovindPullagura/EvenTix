from flask import Blueprint
from controllers.event_controllers import get_all_events, get_one_event, add_event, edit_event, delete_event, add_events


event_router = Blueprint('event', __name__)

event_router.route('/', methods=['GET'])(get_all_events)
event_router.route('/<event_id>', methods=['GET'])(get_one_event)
event_router.route('/addEvent', methods=["POST"])(add_event)
event_router.route('/addEvents', methods=["POST"])(add_events)
event_router.route('/editEvent/<event_id>', methods=['PATCH'])(edit_event)
event_router.route('/deleteEvent/<event_id>', methods=['DELETE'])(delete_event)
