from flask import url_for


def test_get_colors_by_photo_id(app_with_data):
    response = app_with_data.get(url_for("results-service.colors.get_colors_by_photo_id", photo_id=1))

    assert response.status_code == 200
    data = response.json
    assert(data == [{'red': 100, 'green': 100, 'blue': 100}])
