from models_results_service.domain import Object, PhotoObject
from models_results_service.domain.dal import create_session
from models_results_service.modules.labels.objects.commands.new_objects_command import NewObjectCommand
from models_results_service.modules.labels.objects.queries.get_objects_query import GetObjectQuery


class NewPhotoObjectCommand:
    def __init__(self):
        pass

    @staticmethod
    def create(object_entity: Object, photo_id: int):
        object = GetObjectQuery().by_name(object_entity.name)

        if not object:
            object_id = NewObjectCommand().create(object_entity)
        else:
            object_id = object.id
        current_session = create_session()
        try:
            current_session.add(PhotoObject(photo_id=photo_id,
                                            object_id=object_id))
            current_session.commit()

        finally:
            current_session.close()
