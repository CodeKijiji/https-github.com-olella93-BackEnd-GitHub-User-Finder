from flask import Flask, request
from flask_cors import CORS
from server.config import Config
from server.extensions import db, jwt, migrate, limiter

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(
        app,
        resources={r"/api/*": {"origins": "*"}},
        supports_credentials=True,
        methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
        allow_headers=["Content-Type", "Authorization"],
        expose_headers=["Content-Type", "X-Total-Count"],
        max_age=86400
    )

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    limiter.init_app(app)

    # ✅ Register blueprints
    from server.controllers.auth_controller import auth_bp
    from server.controllers.user_controller import user_bp
    from server.controllers.item_controller import item_bp
    from server.controllers.comment_controller import comment_bp
    from server.controllers.search_controller import search_bp

    app.register_blueprint(auth_bp, url_prefix="/api")
    app.register_blueprint(user_bp, url_prefix="/api")
    app.register_blueprint(item_bp, url_prefix="/api/items")
    app.register_blueprint(comment_bp, url_prefix="/api/comments")
    app.register_blueprint(search_bp, url_prefix="/api")

    # Health check
    @app.route("/", methods=["GET"])
    def health_check():
        return {"message": "Backend is live"}, 200

    # Debug CORS logs (optional)
    @app.after_request
    def after_request(response):
        app.logger.info(
            f"CORS Debug - Origin: {request.headers.get('Origin')} | "
            f"Method: {request.method} | "
            f"Path: {request.path} | "
            f"Status: {response.status_code}"
        )
        return response

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
