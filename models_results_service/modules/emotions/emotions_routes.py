from flask import Blueprint

from models_results_service.modules.emotions.queries.get_emotions_query import GetEmotionsQuery

emotions_blueprint = Blueprint('emotions', __name__, url_prefix='/emotions')


@emotions_blueprint.route('/<int:photo_id>', methods=['GET'])
def get_emotions_by_photo_id(photo_id):
    emotions = GetEmotionsQuery().by_photo_id(photo_id)
    emotions_response = [emotion.name for emotion in emotions]

    return emotions_response
