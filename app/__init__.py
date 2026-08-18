from flask import Flask, jsonify, request
from app.routes.users_routes import users_bp

def create_app():
    app = Flask(__name__)

    # Rotas simples de teste
    @app.route("/", methods=["GET"])
    def home():
        return jsonify({"message": "API Connect funcionando!"}), 200

    @app.route("/echo", methods=["POST"])
    def echo():
        data = request.get_json()
        return jsonify({"received": data}), 201

    # Registro do blueprint de usuários
    app.register_blueprint(users_bp)

    return app
