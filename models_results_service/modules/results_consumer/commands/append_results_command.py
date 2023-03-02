import logging

from models_results_service.domain import PhotoColor, Object, Emotion, Association
from models_results_service.modules.results.associations.commands.new_photo_association_command import \
    NewPhotoAssociationCommand
from models_results_service.modules.results.associations.schemas.association_schema import AssociationSchema
from models_results_service.modules.results.colors.commands.new_photo_color_command import NewPhotoColorCommand
from models_results_service.modules.results.colors.schemas.photo_color_schema import PhotoColorSchema
from models_results_service.modules.results.emotions.commands.new_photo_emotion_command import NewPhotoEmotionCommand
from models_results_service.modules.results.emotions.schemas.emotion_schema import EmotionSchema
from models_results_service.modules.results.objects.commands.new_photo_object_command import NewPhotoObjectCommand
from models_results_service.modules.results.objects.schemas.object_schema import ObjectSchema

insert_to_db_commands = {
    'emotion': NewPhotoEmotionCommand,
    'objects': NewPhotoObjectCommand,
    'colors': NewPhotoColorCommand,
    'association': NewPhotoAssociationCommand,
}

map_result_to_entity = {
    'emotion': Emotion,
    'objects': Object,
    'colors': PhotoColor,
    'association': Association,
}

validate_result_with_schema = {
    'emotion': EmotionSchema,
    'objects': ObjectSchema,
    'colors': PhotoColorSchema,
    'association': AssociationSchema,
}


class AppendResultsCommand:
    @staticmethod
    def execute(result_message):
        model_type = result_message['model_type']

        for result in result_message['result']:
            try:
                valid_result = validate_result_with_schema[model_type](**result)
                result_entity = map_result_to_entity[model_type](**valid_result.dict())

                insert_to_db_command = insert_to_db_commands[model_type]
                insert_to_db_command().create(result_entity, result_message['photo_id'])

            except Exception as e:
                logging.error('Something went wrong! ' + str(e))
