from models_results_service.domain import Emotion
from models_results_service.domain.data_access_layer.session import session


class NewEmotionCommand:
    def __init__(self):
        pass

    @staticmethod
    def create(emotion_entity: Emotion) -> int:
        current_session = session()
        try:
            current_session.add(emotion_entity)
            current_session.commit()
            return emotion_entity.id
        finally:
            current_session.close()