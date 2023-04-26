import pytest
from sqlalchemy import delete

from application import create_app
from models_results_service.domain import PhotoColor
from models_results_service.domain.data_access_layer.db import db
from models_results_service.domain.data_access_layer.session import session


@pytest.fixture
def flask_app():
    app = create_app()

    client = app.test_client()

    ctx = app.test_request_context()
    ctx.push()

    yield client
    ctx.pop()


@pytest.fixture
def app_with_db(flask_app):
    db.create_all()

    yield flask_app

    with session() as current_session:
        current_session.commit()
    db.drop_all()


@pytest.fixture
def app_with_data(app_with_db):
    photo_color = PhotoColor()
    photo_color.photo_id = 1
    photo_color.red = 100
    photo_color.green = 100
    photo_color.blue = 100

    with session() as current_session:
        current_session.add(photo_color)
        current_session.commit()

    yield app_with_db

    with session() as current_session:
        current_session.execute(delete(PhotoColor))
        current_session.commit()
