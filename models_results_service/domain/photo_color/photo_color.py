from models_results_service.domain.dal import db


class PhotoColor(db.Model):
    __tablename__ = 'photo_color'

    # id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)

    photo_id = db.Column(db.Integer, nullable=False, primary_key=True)
    red = db.Column(db.Integer, nullable=False, primary_key=True)
    green = db.Column(db.Integer, nullable=False, primary_key=True)
    blue = db.Column(db.Integer, nullable=False, primary_key=True)

    def __repr__(self):
        return f'<Color photo_id: {self.photo_id!r} red:{self.red!r} green:{self.green!r} blue:{self.blue!r}>'
