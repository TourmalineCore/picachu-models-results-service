from models_results_service.config import rabbitmq_results_queue_name
from models_results_service.rabbitmq.rabbitmq_consumer import RabbitMqConsumer
from models_results_service.results_consumer.commands.append_results_command import AppendResultsCommand

queue_name = rabbitmq_results_queue_name


def process_result(message):
    AppendResultsCommand().execute(message)


def start_results_consumer():
    RabbitMqConsumer(
        queue_name,
        process_result,
    ).start()
