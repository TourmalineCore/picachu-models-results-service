from models_results_service.domain import Object, PhotoObject
from models_results_service.domain.dal import create_session
from models_results_service.modules.labels.general.get_from_db_or_create.get_from_db_or_create import \
    get_from_db_or_create


class NewPhotoObjectCommand:
    def __init__(self):
        pass

    @staticmethod
    def create(object_entity: Object, photo_id: int):
        object_id = get_from_db_or_create(Object, name=object_entity.name).id

        with create_session() as current_session:
            current_session.add(PhotoObject(photo_id=photo_id,
                                            object_id=object_id))
            current_session.commit()
