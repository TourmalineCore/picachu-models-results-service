from models_results_service.domain import Association, PhotoAssociation
from models_results_service.domain.dal import create_session
from models_results_service.modules.labels.associations.commands.new_association_command import NewAssociationCommand
from models_results_service.modules.labels.associations.queries.get_associations_query import GetAssociationQuery


class NewPhotoAssociationCommand:
    def __init__(self):
        pass

    @staticmethod
    def create(association_entity: Association, photo_id: int):
        association = GetAssociationQuery().by_name(association_entity.name)

        if not association:
            association_id = NewAssociationCommand().create(association_entity)
        else:
            association_id = association.id

        current_session = create_session()

        try:
            current_session.add(PhotoAssociation(photo_id=photo_id,
                                                 association_id=association_id))
            current_session.commit()

        finally:
            current_session.close()
