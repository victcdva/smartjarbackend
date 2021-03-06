from flask import Flask
from flask_cors import CORS

# https://gist.github.com/randallreedjr/aa89e069371d07371882eea2df15fb4d


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    CORS(app)

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from models import db
    db.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=False)
