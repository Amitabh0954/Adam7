from flask import Flask
from backend.config.config import config
from backend.models.user import init_db
from backend.controllers.users.user_controller import user_bp

# Initialize Flask app
app = Flask(__name__)

# Load Config
app.config.from_object(config)

# Initialize DB
init_db(app)

# Register Blueprints
app.register_blueprint(user_bp, url_prefix='/users')

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=config.LOGGING_LEVEL)
    app.run(host='0.0.0.0', port=5000)