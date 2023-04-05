from models_results_service.domain import Association, PhotoAssociation
from models_results_service.domain.data_access_layer.session import session


class GetAssociationQuery:

    def __init__(self):
        pass

    def by_photo_id(self, photo_id):
        with session() as current_session:
            return current_session \
                .query(Association) \
                .join(PhotoAssociation) \
                .filter(PhotoAssociation.photo_id == photo_id) \
                .all()

    def by_name(self, association_name):
        with session() as current_session:
            return current_session \
                .query(Association) \
                .filter(Association.name == association_name) \
                .one_or_none()
