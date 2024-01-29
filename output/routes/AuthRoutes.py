from flask import Blueprint
from controllers import AuthController

auth_routes = Blueprint('auth_routes', __name__)

auth_routes.route('/signup', methods=['GET'])(AuthController.signup_get)
auth_routes.route('/signup', methods=['POST'])(AuthController.signup_post)
auth_routes.route('/login', methods=['GET'])(AuthController.login_get)
auth_routes.route('/login', methods=['POST'])(AuthController.login_post)
auth_routes.route('/auth', methods=['POST'])(AuthController.auth)
