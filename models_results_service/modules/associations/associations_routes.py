from flask import Blueprint

from models_results_service.modules.associations.queries.get_associations_query import GetAssociationsQuery

associations_blueprint = Blueprint('associations', __name__, url_prefix='/associations')


@associations_blueprint.route('/<int:photo_id>', methods=['GET'])
def get_associations_by_photo_id(photo_id):
    associations = GetAssociationsQuery().by_photo_id(photo_id)
    associations_response = [association.name for association in associations]

    return associations_response
