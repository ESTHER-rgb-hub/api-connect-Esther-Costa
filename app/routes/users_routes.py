from flask import Blueprint, request, jsonify
from app.controllers.users_controller import list_users, create_user
from app.data.users_data import users

users_bp = Blueprint("users", __name__)

# Rota GET para listar usuários
@users_bp.route("/users", methods=["GET"])
def get_users():
    all_users = list_users()
    return jsonify(all_users), 200

# Rota POST para cadastrar usuário
@users_bp.route("/users", methods=["POST"])
def post_user():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "Nome e email são obrigatórios"}), 400

    new_user = create_user(name, email)
    return jsonify(new_user), 201

# Rota GET para buscar usuário por ID
@users_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "Usuário não encontrado"}), 404

# Rota PUT/PATCH para atualizar usuário
@users_bp.route("/users/<int:user_id>", methods=["PUT", "PATCH"])
def update_user(user_id):
    data = request.get_json()
    user = next((u for u in users if u["id"] == user_id), None)

    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404

    if "name" in data:
        user["name"] = data["name"]
    if "email" in data:
        user["email"] = data["email"]

    return jsonify(user), 200

# Rota DELETE para remover usuário
@users_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)

    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404

    users.remove(user)
    return jsonify({"message": "Usuário removido com sucesso"}), 200
    # ou: return "", 204

