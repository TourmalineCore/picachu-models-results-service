from flask import Blueprint

import time

from models_results_service.modules.tags.associations.queries.get_associations_query import GetAssociationQuery
from models_results_service.modules.tags.colors.queries.get_colors_query import GetColorQuery
from models_results_service.modules.tags.emotions.queries.get_emotions_query import GetEmotionQuery
from models_results_service.modules.tags.general.queries.get_photo_query import GetPhotoQuery
from models_results_service.modules.tags.general.schemas.labels_response_schema import LabelsResponseSchema
from models_results_service.modules.tags.objects.queries.get_objects_query import GetObjectQuery

labels_blueprint = Blueprint('tags', __name__, url_prefix='/tags')


@labels_blueprint.route('/<photo_id>', methods=['GET'])
def get_labels_by_photo_id(photo_id: str):
    while True:
        emotions_response = GetEmotionQuery().by_photo_id(photo_id)
        if emotions_response is None:
            continue
        else:
            emotion_name = emotions_response.name
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
        color_response = list(map(lambda color: {"red": color.red, "green": color.green, "blue": color.blue},
                                  GetColorQuery().by_photo_id(photo_id)))
        break

    while True:
        associations_response = GetAssociationQuery().by_photo_id(photo_id)
        if not associations_response:
            continue
        associations_response = [association.name for association in GetAssociationQuery().by_photo_id(photo_id)]
        break

    return {
        'objects': objects_response,
        'emotions': emotions_response,
        'colors': color_response,
        'associations': associations_response,
    }


@labels_blueprint.route('/', methods=['GET'])
def get_photo_with_model_results_but_without_associations():
    photos_with_model_results_but_without_associations = GetPhotoQuery().with_model_results_but_without_associative_tags()
    photo_ids = list(map(lambda photo: photo.photo_id, photos_with_model_results_but_without_associations))

    labels_response = []
    for photo_id in photo_ids:
        photo_tags = []
        photo_tags.extend([object_.name for object_ in GetObjectQuery().by_photo_id(photo_id)])
        photo_tags.extend([emotion.name for emotion in GetEmotionQuery().by_photo_id(photo_id)])

        labels_response.append(LabelsResponseSchema(photo_id=photo_id, tags=photo_tags).dict())

    return labels_response
