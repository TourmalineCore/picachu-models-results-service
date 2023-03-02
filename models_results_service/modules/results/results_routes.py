from flask import Blueprint

import time

from models_results_service.modules.results.associations.queries.get_associations_query import GetAssociationQuery
from models_results_service.modules.results.colors.queries.get_colors_query import GetColorQuery
from models_results_service.modules.results.emotions.queries.get_emotions_query import GetEmotionQuery
from models_results_service.modules.results.general.queries.get_photo_query import GetPhotoQuery
from models_results_service.modules.results.general.schemas.results_response_schema import ResultsResponseSchema
from models_results_service.modules.results.objects.queries.get_objects_query import GetObjectQuery

results_blueprint = Blueprint('results', __name__, url_prefix='/results')


@results_blueprint.route('/<photo_id>', methods=['GET'])
def get_results_by_photo_id(photo_id: str):
    while True:
        emotions_response = GetEmotionQuery().by_photo_id(photo_id)
        if emotions_response is None:
            continue
        time.sleep(5)
        emotions_response = [emotion.name for emotion in GetEmotionQuery().by_photo_id(photo_id)]
        break

    while True:
        objects_response = GetObjectQuery().by_photo_id(photo_id)
        if not objects_response:
            continue
        time.sleep(5)
        objects_response = [object_.name for object_ in GetObjectQuery().by_photo_id(photo_id)]
        break

    while True:
        color_response = GetColorQuery().by_photo_id(photo_id)
        if not color_response:
            continue
        time.sleep(5)
        color_response = list(map(lambda color: {"red": color.red, "green": color.green, "blue": color.blue},
                                  GetColorQuery().by_photo_id(photo_id)))
        break

    while True:
        associations_response = GetAssociationQuery().by_photo_id(photo_id)
        if not associations_response:
            continue
        time.sleep(5)
        associations_response = [association.name for association in GetAssociationQuery().by_photo_id(photo_id)]
        break

    return {
        'objects': objects_response,
        'emotions': emotions_response,
        'colors': color_response,
        'associations': associations_response,
    }


@results_blueprint.route('/', methods=['GET'])
def get_photo_with_model_results_but_without_associations():
    photos_with_model_results_but_without_associations = GetPhotoQuery().with_model_results_but_without_associations()
    photo_ids = list(map(lambda photo: photo.photo_id, photos_with_model_results_but_without_associations))

    results_response = []
    for photo_id in photo_ids:
        photo_tags = []
        photo_tags.extend([object_.name for object_ in GetObjectQuery().by_photo_id(photo_id)])
        photo_tags.extend([emotion.name for emotion in GetEmotionQuery().by_photo_id(photo_id)])

        results_response.append(ResultsResponseSchema(photo_id=photo_id, tags=photo_tags).dict())

    return results_response
