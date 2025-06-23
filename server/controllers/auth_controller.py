from flask import Blueprint, request, jsonify
from server.extensions import db, limiter
from server.models.user import User
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from sqlalchemy.exc import IntegrityError

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/register", methods=["POST"])
@limiter.limit("5 per minute")
def register():
    data = request.get_json()
    try:
        user = User(
            username=data["username"],
            email=data["email"]
        )
        user.password_hash = data["password"]
        db.session.add(user)
        db.session.commit()

        token = create_access_token(identity=user.id)
        return jsonify(access_token=token), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify(error="Username or email already exists."), 409
    except Exception as e:
        return jsonify(error=str(e)), 400

@auth_bp.route("/login", methods=["POST"])
@limiter.limit("10 per minute")
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data.get("username")).first()

    if user and user.check_password(data.get("password")):
        token = create_access_token(identity=user.id)
        return jsonify(access_token=token), 200
    return jsonify(error="Invalid credentials"), 401
