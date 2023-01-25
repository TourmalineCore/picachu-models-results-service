from flask import Flask, Blueprint
from flask_migrate import upgrade as _upgrade
from flask_cors import CORS

from models_results_service.domain.dal import build_connection_string, db, migrate
from models_results_service.modules.labels.labels_routes import labels_blueprint
from models_results_service.results_consumer.results_consumer import start_results_consumer


def create_app():
    """Application factory, used to create application"""
    app = Flask(__name__)
    app.config.from_object('models_results_service.config')

    # without this /feeds will work but /feeds/ with the slash at the end won't
    app.url_map.strict_slashes = False

    # allow to call the api from any origin for now
    CORS(
        app,
    )

    app.config['SQLALCHEMY_DATABASE_URI'] = build_connection_string()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    register_blueprints(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # runs pending migrations
    with app.app_context():
        _upgrade()

    start_results_consumer()

    return app


def register_blueprints(app):
    """Register all blueprints for application"""
    results_blueprint = Blueprint('results', __name__, url_prefix='/results')
    results_blueprint.register_blueprint(labels_blueprint)

    app.register_blueprint(results_blueprint)
