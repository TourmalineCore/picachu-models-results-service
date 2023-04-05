from flask import Blueprint

from models_results_service.modules.emotions.queries.get_emotions_query import GetEmotionsQuery
from models_results_service.modules.objects.queries.get_objects_query import GetObjectsQuery
from models_results_service.modules.results.queries.get_photo_query import GetPhotoQuery
from models_results_service.modules.results.schemas.results_response_schema import ResultsResponseSchema

results_blueprint = Blueprint('results', __name__, url_prefix='/results')


@results_blueprint.route('/', methods=['GET'])
def get_photo_with_model_results_but_without_associations():
    photos_with_model_results_but_without_associations = GetPhotoQuery().with_model_results_but_without_associations()
    photo_ids = list(map(lambda photo: photo.photo_id, photos_with_model_results_but_without_associations))

    results_response = []
    for photo_id in photo_ids:
        photo_tags = []
        photo_tags.extend([object_.name for object_ in GetObjectsQuery().by_photo_id(photo_id)])
        photo_tags.extend([emotion.name for emotion in GetEmotionsQuery().by_photo_id(photo_id)])

        results_response.append(ResultsResponseSchema(photo_id=photo_id, tags=photo_tags).dict())

    return results_response
