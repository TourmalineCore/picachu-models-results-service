from models_results_service.config import rabbitmq_models_results_queue_name
from models_results_service.modules.models_results.commands.append_results_command import AppendResultsCommand
from models_results_service.consumer_base.consumer_base import ConsumerBase


def process_result(message):
    AppendResultsCommand().execute(message)


def start_results_consumer():
    ConsumerBase(
        rabbitmq_models_results_queue_name,
        process_result,
    ).start()
