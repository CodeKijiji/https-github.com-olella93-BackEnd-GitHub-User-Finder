from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models.item import Item
from server.extensions import db

item_bp = Blueprint("item_bp", __name__, url_prefix="/api/items")

@item_bp.route("/", methods=["POST"])
@jwt_required()
def create_item():
    data = request.get_json()

    if not all(field in data for field in ["name", "description", "category"]):
        return jsonify(error="Missing required fields"), 400

    item = Item(
        name=data["name"],
        description=data["description"],
        category=data["category"]
    )

    db.session.add(item)
    db.session.commit()

    return jsonify(item.to_dict()), 201


@item_bp.route("/", methods=["GET"])
@jwt_required()
def get_items():
    category = request.args.get("category")
    if category:
        items = Item.query.filter_by(category=category).all()
    else:
        items = Item.query.all()

    return jsonify([item.to_dict() for item in items]), 200


@item_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_item(id):
    item = Item.query.get(id)
    if not item:
        return jsonify(error="Item not found"), 404

    data = request.get_json()
    item.name = data.get("name", item.name)
    item.description = data.get("description", item.description)
    item.category = data.get("category", item.category)

    db.session.commit()
    return jsonify(item.to_dict()), 200


@item_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_item(id):
    item = Item.query.get(id)
    if not item:
        return jsonify(error="Item not found"), 404

    db.session.delete(item)
    db.session.commit()
    return jsonify(message="Item deleted"), 200
