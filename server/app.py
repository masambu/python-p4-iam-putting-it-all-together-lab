#!/usr/bin/env python3

from flask import request, session, jsonify
from flask_restful import Resource
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError

from config import app, db, api
from models import User, Recipe

class Signup(Resource):
    def post(self):
        data= request.get_json()

        username = data.get('username')
        password=data.get('password')
        image_url = data.get('image_url')
        bio = data.get('bio')

        encrypted_password = generate_password_hash(password)

        new_user = User(username=username, password= encrypted_password,image_url=image_url, bio=bio)

        db.sesion.add(new_user)
        db.session.commit()

        session['user_id'] = new_user.id

        response_data = {
            'id': new_user.id,
            'username':new_user.username,
            'image_url': new_user.image_url,
            'bio': new_user.bio
        }

        return jsonify(response_data), 201

class CheckSession(Resource):
    pass

class Login(Resource):
    pass

class Logout(Resource):
    pass

class RecipeIndex(Resource):
    pass

api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')
api.add_resource(RecipeIndex, '/recipes', endpoint='recipes')


if __name__ == '__main__':
    app.run(port=5555, debug=True)