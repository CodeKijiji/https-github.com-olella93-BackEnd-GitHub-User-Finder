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
            Item.name.ilike(f"%{query}%"),
            Item.description.ilike(f"%{query}%")
        )
    ).all()

    items_data = [
        {
            "id": item.id,
            "name": item.name,
            "description": item.description,
            "category": item.category,
            "created_at": item.created_at.isoformat()
        }
        for item in results
    ]

    return jsonify(items_data), 200
