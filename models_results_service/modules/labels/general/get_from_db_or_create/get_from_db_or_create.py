from models_results_service.domain.dal import create_session


def get_from_db_or_create(model, **kwargs):
    with create_session() as session:
        instance = session \
            .query(model) \
            .filter_by(**kwargs)\
            .first()

        if instance:
            return instance
        else:
            instance = model(**kwargs)
            session.add(instance)
            session.commit()
            return instance
