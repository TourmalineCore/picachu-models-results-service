from config import rabbitmq_results_queue_name
from rabbitmq.rabbitmq_consumer import RabbitMqConsumer
from results_consumer.commands.append_results_command import AppendResultsCommand

queue_name = rabbitmq_results_queue_name


def process_result(message):
    AppendResultsCommand().execute(message)


if __name__ == '__main__':
    RabbitMqConsumer(
        queue_name,
        process_result,
    ).run()
