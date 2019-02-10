from app.api.v1.models.db import Database
from werkzeug.security import generate_password_hash
import json


class UsersModel(Database):
	"""Initialization."""

	def __init__(self,firstname=None,lastname=None,othername=None,email=None,password=None,phoneNumber=None,passportUrl=None,role=None):

		super().__init__()
		self.firstname = firstname
		self.lastname = lastname
		self.othername = othername
		self.email = email
		if password:
			self.password = generate_password_hash(password)
		self.phoneNumber = phoneNumber
		self.passportUrl = passportUrl
		self.role = role

	def save(self,firstname,lastname,othername,email,password,phoneNumber,passportUrl,role):
		"""Save information of the new user"""

		self.curr.execute(
            ''' INSERT INTO users(firstname,lastname,othername,email,password,phoneNumber,passportUrl,role)\
             VALUES('{}','{}','{}','{}','{}','{}','{}','{}') RETURNING firstname,lastname,othername,email,password,phoneNumber,passportUrl,role'''\
            .format(firstname,lastname,othername,email,password,phoneNumber,passportUrl,role))
		create = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return create

	def get_users(self):
		"""Fetch all users"""

		self.curr.execute(''' SELECT * FROM users''')
		users = self.curr.fetchall()
		self.conn.commit()
		self.curr.close()
		return users

	def get_user_by_id(self, user_id):
		"""Fetch a single user by ID"""

		self.curr.execute(""" SELECT * FROM users WHERE user_id={}""".format(user_id))
		user = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return user