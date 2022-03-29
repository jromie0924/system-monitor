from pika.adapters.blocking_connection import BlockingChannel, BlockingConnection
from config import Config
from common import Common


class Publisher():
  _connection: BlockingConnection = None
  _channel: BlockingChannel = None
  
  def __init__(self, url, exchange, routing_key) -> None:
    common = Common()
    self._connection = common.open_connection(url)
    self._exchange = exchange
    self._routing_key = routing_key
    self._channel = self._connection.channel()

  def publish_message(self, message):
    # TODO: add properties for headers: properties=pika.BasicProperties(headers={"key": "value"})
    self._channel.basic_publish(self._exchange, routing_key=self._routing_key, body=message)


if __name__ == '__main__':
  config = Config()

  try:
    url = f'amqp://{config.mq_username}:{config.mq_password}@{config.mq_url}:{config.mq_port}'
    exchange = config.mq_emergency_exchange
    routing_key = config.mq_emergency_queue
    publisher = Publisher(url=url, exchange=exchange, routing_key=routing_key)

    while True:
      msg = input('Enter a message to publish: ')
      publisher.publish_message(msg)
  except KeyboardInterrupt:
    exit(0)
