from models_results_service.domain.data_access_layer.session import session

from models_results_service.domain import Object


class NewObjectCommand:
    def __init__(self):
        pass

    @staticmethod
    def create(object_entity: Object) -> int:
        current_session = session()
        try:
            current_session.add(object_entity)
            current_session.commit()
            return object_entity.id
        finally:
            current_session.close()