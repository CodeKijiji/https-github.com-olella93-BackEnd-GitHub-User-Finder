from flask import Flask
from flask_cors import CORS
from server.config import Config
from server.extensions import db, jwt, migrate, limiter

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Enhanced CORS configuration
    CORS(
        app,
        resources={
            r"/api/*": {
                "origins": [
                    "http://localhost:5173", 
                    "https://https-github-com-olella93-frontend.onrender.com",  
                    "https://github-com-olella93-frontend.onrender.com"  
                ],
                "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                "allow_headers": ["Content-Type", "Authorization"],
                "supports_credentials": True,
                "max_age": 86400 
            }
        }
    )

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    limiter.init_app(app)

    # Register blueprints
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

    return app

app = create_app()