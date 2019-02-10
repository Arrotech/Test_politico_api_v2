from flask import Flask, Blueprint, request, jsonify, make_response
from app.api.v1.views.auth_views import signup
from app.config import app_config
import os

def page_not_found(e):
	"""Capture Not Found error"""

	return make_response(jsonify({
		"status" : "not found",
		"message" : "url does not exist"
		}), 404)


def politico_app(config_name):
	"""Create app """

	app = Flask(__name__)
	#app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')
	app.config["SECRET_KEY"] = 'thisisarrotech'

	app.register_blueprint(signup, url_prefix='/api/v2/auth')
	app.register_error_handler(404, page_not_found)
	
	return app