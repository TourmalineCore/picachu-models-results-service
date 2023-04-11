import pytest
from sqlalchemy import delete

from application import create_app
from models_results_service.domain import PhotoColor
from models_results_service.domain.data_access_layer.db import db


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

    db.session.commit()
    db.drop_all()


@pytest.fixture
def app_with_data(app_with_db):
    photo_color = PhotoColor()
    photo_color.photo_id = 1
    photo_color.red = 100
    photo_color.green = 100
    photo_color.blue = 100
    db.session.add(photo_color)
    db.session.commit()

    yield app_with_db

    db.session.execute(delete(PhotoColor))
    db.session.commit()
