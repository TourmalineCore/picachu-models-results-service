from models_results_service.domain import PhotoAssociation, PhotoColor, PhotoEmotion, PhotoObject
from models_results_service.domain.dal import create_session


class GetPhotoQuery:
    def __init__(self):
        pass

    @staticmethod
    def with_model_results_but_without_associative_tags():
        current_session = create_session()

        try:
            photos_with_color_tags = current_session \
                .query(PhotoColor.photo_id)

            photos_with_emotion_tags = current_session \
                .query(PhotoEmotion.photo_id)

            photos_with_object_tags = current_session \
                .query(PhotoObject.photo_id)

            photos_with_association_tags = current_session \
                .query(PhotoAssociation.photo_id)

            return photos_with_color_tags \
                .intersect(photos_with_emotion_tags) \
                .intersect(photos_with_object_tags) \
                .except_(photos_with_association_tags) \
                .all()

        finally:
            current_session.close()
