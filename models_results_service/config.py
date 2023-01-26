"""Сonfiguration
Use env var to override
"""
import os

ENV = os.getenv('FLASK_ENV')
DEBUG = ENV == 'development'

rabbitmq_host = os.getenv('RABBITMQ_HOST')
rabbitmq_username = os.getenv('RABBITMQ_DEFAULT_USER')
rabbitmq_password = os.getenv('RABBITMQ_DEFAULT_PASS')

rabbitmq_models_results_queue_name = os.getenv('RABBITMQ_MODELS_RESULTS_QUEUE_NAME')


if not rabbitmq_host:
    raise ValueError('You should specify RABBITMQ_HOST to be able to connect to RabbitMQ.')
if not rabbitmq_username:
    raise ValueError('You should specify RABBITMQ_DEFAULT_USER to be able to connect to RabbitMQ.')
if not rabbitmq_password:
    raise ValueError('You should specify RABBITMQ_DEFAULT_PASS to be able to connect to RabbitMQ.')

if not rabbitmq_models_results_queue_name:
    raise ValueError('You should specify RABBITMQ_MODELS_RESULTS_QUEUE_NAME to be able to connect to models_results queue.')
