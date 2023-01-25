from models_results_service.domain.dal import db


class Object(db.Model):
    __tablename__ = 'objects'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(2048), nullable=False)

    photo_object = db.relationship("PhotoObject", back_populates='object')
    # photos = db.relationship(
    #     'PhotoObject',
    #     backref='objects',
    #     lazy='dynamic'
    # )

    def __repr__(self):
        return f'<Object {self.id!r} name:{self.name!r}>'
