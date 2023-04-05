from flask import Flask, Blueprint
from flask_migrate import upgrade as _upgrade
from flask_cors import CORS

from models_results_service.domain.data_access_layer.build_connection_string import build_connection_string
from models_results_service.domain.data_access_layer.db import db, migrate
from models_results_service.modules.associations.associations_routes import associations_blueprint
from models_results_service.modules.colors.colors_routes import colors_blueprint
from models_results_service.modules.emotions.emotions_routes import emotions_blueprint
from models_results_service.modules.objects.objects_routes import objects_blueprint
from models_results_service.modules.results.results_routes import results_blueprint

from models_results_service.modules.results_consumer.results_consumer import start_results_consumer


def create_app():
    """Application factory, used to create application"""
    app = Flask(__name__)
    app.config.from_object('models_results_service.config.flask_config')

    app.url_map.strict_slashes = False

    CORS(
        app,
    )

    app.config['SQLALCHEMY_DATABASE_URI'] = build_connection_string()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    register_blueprints(app)
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        _upgrade()

    start_results_consumer()

    return app


def register_blueprints(app):
    """Register all blueprints for application"""
    results_service_blueprint = Blueprint('results-service', __name__, url_prefix='/results-service')
    results_service_blueprint.register_blueprint(results_blueprint)
    results_service_blueprint.register_blueprint(associations_blueprint)
    results_service_blueprint.register_blueprint(colors_blueprint)
    results_service_blueprint.register_blueprint(emotions_blueprint)
    results_service_blueprint.register_blueprint(objects_blueprint)

    app.register_blueprint(results_service_blueprint)
