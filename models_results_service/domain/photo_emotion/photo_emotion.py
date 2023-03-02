from models_results_service.domain.data_access_layer.db import db



class PhotoEmotion(db.Model):
    __tablename__ = 'photo_emotion'

    photo_id = db.Column(db.BigInteger, nullable=False, primary_key=True)
    emotion_id = db.Column(db.BigInteger, db.ForeignKey('emotions.id'), primary_key=True)

    emotion = db.relationship("Emotion", back_populates='photo_emotion')

    def __repr__(self):
        return f'<PhotoEmotion photo_id:{self.photo_id!r} emotion_id:{self.emotion_id!r}>'
