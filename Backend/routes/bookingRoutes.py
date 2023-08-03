from flask import Blueprint
from controllers.booking_controllers import get_all_bookings, book_event, delete_booking, get_user_bookings


booking_router = Blueprint('booking', __name__)

booking_router.route('/', methods=['GET'])(get_all_bookings)
booking_router.route('/<user_id>', methods=['GET'])(get_user_bookings)
booking_router.route('/placeOrder', methods=['POST'])(book_event)
booking_router.route('/deleteBooking', methods=['DELETE'])(delete_booking)
