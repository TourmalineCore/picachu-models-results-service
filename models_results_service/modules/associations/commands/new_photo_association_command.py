from models_results_service.domain import Association, PhotoAssociation
from models_results_service.domain.data_access_layer.session import session
from models_results_service.modules.results.get_from_db_or_create.get_from_db_or_create import \
    get_from_db_or_create


class NewPhotoAssociationCommand:
    def __init__(self):
        pass

    @staticmethod
    def create(association_entity: Association, photo_id: int):
        association_id = get_from_db_or_create(Association, name=association_entity.name).id

        with session() as current_session:
            current_session.add(PhotoAssociation(photo_id=photo_id,
                                                 association_id=association_id))
            current_session.commit()
