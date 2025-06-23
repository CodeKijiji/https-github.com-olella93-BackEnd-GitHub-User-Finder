from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from server.models.comment import Comment
from server.models.item import Item
from server.models.user import User
from server.extensions import db

comment_bp = Blueprint("comment_bp", __name__, url_prefix="/api/comments")


# POST /api/comments
@comment_bp.route("/", methods=["POST"])
@jwt_required()
def create_comment():
    data = request.get_json()
    user_id = get_jwt_identity()

    content = data.get("content")
    item_id = data.get("item_id")

    if not content or not item_id:
        return jsonify({"error": "Missing content or item_id"}), 400

    comment = Comment(content=content, user_id=user_id, item_id=item_id)
    db.session.add(comment)
    db.session.commit()

    return jsonify({
        "id": comment.id,
        "content": comment.content,
        "user_id": comment.user_id,
        "item_id": comment.item_id
    }), 201


# GET /api/comments/<item_id>
@comment_bp.route("/<int:item_id>", methods=["GET"])
def get_comments(item_id):
    comments = Comment.query.filter_by(item_id=item_id).all()
    return jsonify([
        {
            "id": c.id,
            "content": c.content,
            "user_id": c.user_id,
            "item_id": c.item_id
        } for c in comments
    ]), 200


# DELETE /api/comments/<id>
@comment_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_comment(id):
    user_id = get_jwt_identity()
    comment = Comment.query.get(id)

    if not comment:
        return jsonify({"error": "Comment not found"}), 404

    if comment.user_id != user_id:
        return jsonify({"error": "Not authorized to delete this comment"}), 403

    db.session.delete(comment)
    db.session.commit()
    return jsonify({"message": "Comment deleted"}), 200
