from models_results_service.domain import Emotion, PhotoEmotion
from models_results_service.domain.dal import create_session
from models_results_service.modules.labels.emotions.commands.new_emotion_command import NewEmotionCommand
from models_results_service.modules.labels.emotions.queries.get_emotions_query import GetEmotionQuery


class NewPhotoEmotionCommand:
    def __init__(self):
        pass

    @staticmethod
    def create(emotion_entity: Emotion, photo_id: int):
        emotion = GetEmotionQuery().by_name(emotion_entity.name)

        if not emotion:
            emotion_id = NewEmotionCommand().create(emotion_entity)
        else:
            emotion_id = emotion.id

        current_session = create_session()

        try:
            current_session.add(PhotoEmotion(photo_id=photo_id,
                                             emotion_id=emotion_id))
            current_session.commit()

        finally:
            current_session.close()
