import json
import logging
from threading import Thread

from pika import BlockingConnection, ConnectionParameters, PlainCredentials
from pika.exceptions import ConnectionClosedByBroker, AMQPChannelError, AMQPConnectionError

from models_results_service.config.rabbitmq_config import rabbitmq_host, rabbitmq_username, rabbitmq_password

connection_parameters = ConnectionParameters(
            host=rabbitmq_host,
            credentials=PlainCredentials(rabbitmq_username, rabbitmq_password),
            blocked_connection_timeout=300,
        )


class MessagesConsumerBase(Thread):
    def __init__(
            self,
            queue_name,
            message_handler,
    ):
        self.queue_name = queue_name
        self.message_handler = message_handler

        super().__init__(target=self.start_listening_to_the_queue)

    def start_listening_to_the_queue(self):
        while True:
            try:
                connection = BlockingConnection(connection_parameters)

                channel = connection.channel()
                channel.basic_qos(prefetch_count=1)
                channel.queue_declare(
                    queue=self.queue_name,
                    durable=True,
                    exclusive=False,
                    auto_delete=False,
                )
                channel.basic_consume(self.queue_name, self.request_message_processing)
                channel.start_consuming()
                logging.info('{0} queue consumer started.'.format(self.queue_name))

            except (ConnectionClosedByBroker, AMQPConnectionError):
                logging.info('Connection was closed, retrying...')
                continue

            except AMQPChannelError as e:
                logging.error('Channel error: {0}, stopping...'.format(e))
                break

            except Exception as e:
                logging.error('Unexpected error: {0}'.format(e))

    def request_message_processing(self, channel, method, _, body):
        message = json.loads(body.decode('utf-8'))

        try:
            self.message_handler(message)
            channel.basic_ack(delivery_tag=method.delivery_tag)
        except Exception as e:
            logging.error('Unexpected error: {0}'.format(e))
            channel.basic_reject(delivery_tag=method.delivery_tag, requeue=True)
            return
