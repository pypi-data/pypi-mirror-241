import sys

sys.path.append("..")
from common_packages.message_queue_utils.rabbitmq import RabbitmqQueue
from . import get_config

class TestRabbitmqQueue:

    def test_enqueue(self):
        config: dict = get_config()
        rabbitmq = RabbitmqQueue(
            **config["message_queue"]["rabbitmq"]
        )
        rabbitmq.enqueue("hello world".encode())

    def test_consumer(self):
        config: dict = get_config()
        rabbitmq = RabbitmqQueue(
            **config["message_queue"]["rabbitmq"]
        )
        rabbitmq.consumer()

