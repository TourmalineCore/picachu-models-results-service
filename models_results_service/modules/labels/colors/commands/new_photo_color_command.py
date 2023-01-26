from models_results_service.domain import PhotoColor
from models_results_service.domain.dal import create_session


class NewPhotoColorCommand:
    def __init__(self):
        pass

    @staticmethod
    def create(color_entity: PhotoColor, photo_id: int):
        color_entity.photo_id = photo_id

        with create_session() as current_session:
            current_session.add(color_entity)
            current_session.commit()
