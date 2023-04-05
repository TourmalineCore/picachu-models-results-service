from models_results_service.domain import PhotoAssociation, PhotoColor, PhotoEmotion, PhotoObject
from models_results_service.domain.data_access_layer.session import session


class GetPhotoQuery:
    def __init__(self):
        pass

    @staticmethod
    def with_model_results_but_without_associations():
        current_session = session()

        try:
            photos_with_color = current_session \
                .query(PhotoColor.photo_id)

            photos_with_emotion = current_session \
                .query(PhotoEmotion.photo_id)

            photos_with_object = current_session \
                .query(PhotoObject.photo_id)

            photos_with_association = current_session \
                .query(PhotoAssociation.photo_id)

            return photos_with_color \
                .intersect(photos_with_emotion) \
                .intersect(photos_with_object) \
                .except_(photos_with_association) \
                .all()

        finally:
            current_session.close()
