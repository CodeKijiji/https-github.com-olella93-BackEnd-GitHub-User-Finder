from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from sqlalchemy import or_
from server.models.item import Item

search_bp = Blueprint('search_bp', __name__)

@search_bp.route("/search", methods=["GET"])
@jwt_required()
def search_items():
    query = request.args.get("q", "").strip()

    if not query:
        return jsonify({"error": "Missing search query"}), 400

    results = Item.query.filter(
        or_(
            Item.github_username.ilike(f"%{query}%"),
            Item.note.ilike(f"%{query}%"),
            Item.category.ilike(f"%{query}%")
        )
    ).all()

    items_data = [
        {
            "id": item.id,
            "github_username": item.github_username,
            "note": item.note,
            "category": item.category,
            "user_id": item.user_id
        }
        for item in results
    ]

    return jsonify(items_data), 200
