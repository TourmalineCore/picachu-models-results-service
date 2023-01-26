from models_results_service.domain import PhotoEmotion, Emotion
from models_results_service.domain.dal import create_session


class GetEmotionQuery:

    def __init__(self):
        pass

    def by_photo_id(self, photo_id):
        with create_session() as current_session:
            return current_session \
                .query(Emotion) \
                .join(PhotoEmotion) \
                .filter(PhotoEmotion.photo_id == photo_id) \
                .all()

    def by_name(self, emotion_name):
        with create_session() as current_session:
            return current_session \
                .query(Emotion) \
                .filter(Emotion.name == emotion_name) \
                .one_or_none()
