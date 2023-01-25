from models_results_service.domain.dal import create_session
from models_results_service.domain import PhotoObject, Object


class GetObjectQuery:
    def __init__(self):
        pass

    def by_photo_id(self, photo_id):
        current_session = create_session()
        try:
            return current_session \
                .query(Object) \
                .join(PhotoObject) \
                .filter(PhotoObject.photo_id == photo_id) \
                .all()

        finally:
            current_session.close()

    def by_name(self, object_name):
        current_session = create_session()
        try:
            return current_session \
                .query(Object) \
                .filter(Object.name == object_name) \
                .one_or_none()

        finally:
            current_session.close()