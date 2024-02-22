from flask import Flask, request, jsonify
from controller import backup_route

app = Flask(__name__)

app.register_blueprint(backup_route)

if __name__ == "__main__":
    app.run(debug=True)