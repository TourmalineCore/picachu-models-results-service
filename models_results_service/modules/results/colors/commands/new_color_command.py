from models_results_service.domain import PhotoColor
from models_results_service.domain.data_access_layer.session import session


class NewColorCommand:
    def __init__(self):
        pass

    @staticmethod
    def create_color(color_entity: PhotoColor) -> int:
        current_session = session()
        try:
            current_session.add(color_entity)
            current_session.commit()
            return color_entity.id
        finally:
            current_session.close()
