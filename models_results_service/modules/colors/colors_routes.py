from flask import Blueprint

from models_results_service.modules.colors.queries.get_colors_query import GetColorsQuery

colors_blueprint = Blueprint('colors', __name__, url_prefix='/colors')


@colors_blueprint.route('/<int:photo_id>', methods=['GET'])
def get_colors_by_photo_id(photo_id):
    colors = GetColorsQuery().by_photo_id(photo_id)
    colors_response = list(map(lambda color: {"red": color.red,
                                              "green": color.green,
                                              "blue": color.blue},
                               colors))

    return colors_response
