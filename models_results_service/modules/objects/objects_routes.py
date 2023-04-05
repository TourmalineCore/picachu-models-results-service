from flask import Blueprint

from models_results_service.modules.objects.queries.get_objects_query import GetObjectsQuery

objects_blueprint = Blueprint('objects', __name__, url_prefix='/objects')


@objects_blueprint.route('/<int:photo_id>', methods=['GET'])
def get_objects_by_photo_id(photo_id):
    objects_entities = GetObjectsQuery().by_photo_id(photo_id)
    objects_response = [object_entity.name for object_entity in objects_entities]

    return objects_response
