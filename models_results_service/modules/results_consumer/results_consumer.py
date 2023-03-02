from models_results_service.config.rabbitmq_config import rabbitmq_models_results_queue_name
from models_results_service.modules.models_results_consumer.commands.append_results_command import AppendResultsCommand
from models_results_service.consumer_base.messages_consumer_base import MessagesConsumerBase


def process_result(message):
    # ToDo add switch by result type and call appropriate command or throw an exception
    AppendResultsCommand().execute(message)


def start_results_consumer():
    MessagesConsumerBase(
        rabbitmq_models_results_queue_name,
        process_result,
    ).start()
