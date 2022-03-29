import pika
from pika.adapters.blocking_connection import BlockingChannel, BlockingConnection


class Listener:
  _channel: BlockingChannel = None
  _connection: BlockingConnection = None

  def __init__(self, url, queue, exchange, username, message_handler) -> None:
    self._connection = self.open_connection(url)
    self._message_handler = message_handler
    self._exchange = exchange
    self._queue = queue
    self.setup_channel()
    self._channel.start_consuming()

  def open_connection(self, url):
    return pika.BlockingConnection(pika.URLParameters(url))

  def setup_channel(self):
    self._channel = self._connection.channel()
    self._channel.exchange_declare(
        exchange=self._exchange, exchange_type='fanout')
    self._channel.queue_declare(queue=self._queue)
    self._channel.queue_bind(
        queue=self._queue, exchange=self._exchange, routing_key=self._queue)
    self._channel.basic_consume(
      queue=self._queue, on_message_callback=self._message_handler)
