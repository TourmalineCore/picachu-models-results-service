from models_results_service.domain.data_access_layer.db import db


class Emotion(db.Model):
    __tablename__ = 'emotions'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(2048), nullable=False)

    photo_emotion = db.relationship("PhotoEmotion", back_populates='emotion')

    def __repr__(self):
        return f'<Emotion {self.id!r} name:{self.name!r}>'
