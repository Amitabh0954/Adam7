from flask import Flask, jsonify
from app.config import Config
from app.routes import register_routes

app = Flask(__name__)
app.config.from_object(Config)

register_routes(app)

@app.errorhandler(Exception)
def handle_exception(e):
    response = {'error': str(e)}
    return jsonify(response), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)