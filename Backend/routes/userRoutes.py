from flask import Blueprint

from controllers.user_controllers import user_login, user_signup, edit_profile, delete_user
from middlewares.userAuth import check_profile_access

user_router = Blueprint('user', __name__)

user_router.route('/login', methods=['POST'])(user_login)
user_router.route('/signup', methods=['POST'])(user_signup)

user_router.before_request(check_profile_access)
user_router.route('/editProfile/<user_id>', methods=['PATCH'])(edit_profile)
user_router.route('/deleteUser/<user_id>', methods=['DELETE'])(delete_user)
