from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v1.models.users_model import UsersModel
from utils.validations import raise_error, check_register_keys, is_valid_email, is_valid_url, on_success, is_valid_phone
import json
from werkzeug.security import check_password_hash, generate_password_hash
          
signup = Blueprint('v2',__name__, url_prefix='/api/v2/')

class Register:
    """A user can create a new account."""
    
    @signup.route('/signup', methods=['POST'])
    def post():
        """Create new account."""

        errors = check_register_keys(request)
        if errors:
            return raise_error(400,"Invalid {} key".format(', '.join(errors)))
        details = request.get_json()
        firstname = details['firstname']
        lastname = details['lastname']
        othername = details['othername']
        email = details['email']
        password = generate_password_hash(details['password'])
        phoneNumber = details['phoneNumber']
        passportUrl = details['passportUrl']
        role = details['role']

        if not is_valid_email(email):
            return raise_error(400,"Email is in the wrong format")
        if not is_valid_phone(phoneNumber):
            return raise_error(400,"phone number is in the wrong format")
        if details['firstname'].isalpha()== False:
            return raise_error(400,"firstname is in wrong format")
        if details['lastname'].isalpha()== False:
            return raise_error(400,"lastname is in wrong format")
        if details['othername'].isalpha()== False:
            return raise_error(400,"othername is in wrong format")
        if details['role'].isalpha()== False:
            return raise_error(400,"role is in wrong format")
        if not is_valid_url(passportUrl):
            return raise_error(400,"passportUrl is in the wrong format")

        user = UsersModel().save(firstname, lastname, othername, email, password, phoneNumber, passportUrl, role)
        return on_success(201,"Account created successfully")

    '''@signup.route('/users', methods=['GET'])
    def get():
        """Admin can fetch all users"""

        return make_response(jsonify({
            "message": "All users",
            "Users": UsersModel().get_users()
            }),200)

    @signup.route('/users/<int:user_id>', methods=['GET'])
    def get(user_id):
        """Admin can fetch a single user"""

        user = UsersModel().get_user_by_id(user_id)
        if user:
            return make_response(jsonify({
                "message": "successfully retrieved",
                "user": user
                }))
        return make_response(jsonify({
            "message": "User Not Found"
            }))'''