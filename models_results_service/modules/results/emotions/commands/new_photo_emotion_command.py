from models_results_service.domain import Emotion, PhotoEmotion
from models_results_service.domain.data_access_layer.session import session
from models_results_service.modules.results.emotions.commands.new_emotion_command import NewEmotionCommand
from models_results_service.modules.results.emotions.queries.get_emotions_query import GetEmotionQuery
from models_results_service.modules.results.general.get_from_db_or_create.get_from_db_or_create import \
    get_from_db_or_create


class NewPhotoEmotionCommand:
    def __init__(self):
        pass

    @staticmethod
    def create(emotion_entity: Emotion, photo_id: int):
        emotion_id = get_from_db_or_create(Emotion, name=emotion_entity.name).id

        with session() as current_session:
            current_session.add(PhotoEmotion(photo_id=photo_id,
                                             emotion_id=emotion_id))
            current_session.commit()
