from flask import Blueprint
from controllers.example_controller import example_bp

def register_routes(app):
    app.register_blueprint(example_bp)