from models_results_service.domain import Association
from models_results_service.domain.data_access_layer.session import session


class NewAssociationCommand:
    def __init__(self):
        pass

    @staticmethod
    def create(association_entity: Association) -> int:
        current_session = session()
        try:
            current_session.add(association_entity)
            current_session.commit()
            return association_entity.id
        finally:
            current_session.close()
