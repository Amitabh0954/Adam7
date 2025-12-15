import os
from flask import Flask, jsonify
from config import Config
from routes import register_routes

app = Flask(__name__)
app.config.from_object(Config)

# Register routes
register_routes(app)

# Global error handler
@app.errorhandler(Exception)
def handle_exception(e):
    response = {
        'error': str(e)
    }
    return jsonify(response), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)