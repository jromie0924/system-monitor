from pika.adapters.blocking_connection import BlockingChannel, BlockingConnection
from pika.spec import Basic, BasicProperties
from config import Config
from common import Common
from shutdown import Shutdown_Controller


class Listener:
  _channel: BlockingChannel = None
  _connection: BlockingConnection = None

  def __init__(self, url, queue, exchange, message_handler) -> None:
    common = Common()
    self._config = Config()
    self._connection = common.open_connection(url)
    self._message_handler = message_handler
    self._exchange = exchange
    self._queue = queue
    self.setup_channel()
    self._channel.start_consuming()

  # def open_connection(self, url):
  #   return pika.BlockingConnection(pika.URLParameters(url))

  def setup_channel(self):
    self._channel = self._connection.channel()
    self._channel.exchange_declare(
        exchange=self._exchange, exchange_type='fanout')
    self._channel.queue_declare(queue=self._queue)
    self._channel.queue_bind(
        queue=self._queue, exchange=self._exchange, routing_key=self._queue)
    self._channel.basic_consume(
      queue=self._queue, on_message_callback=self._message_handler)

def message_handler(ch: BlockingChannel, delivery_args: Basic.Deliver, properties: BasicProperties, body: bytes):
  message = body.decode()

  # TODO: handle headers
  ch.basic_ack(delivery_tag=delivery_args.delivery_tag, multiple=True)
  if message == Config().SHUTDOWN_BODY:
    controller = Shutdown_Controller()
    controller.countdown(30)

if __name__ == '__main__':
  config = Config()

  try:
    url = f'amqp://{config.mq_username}:{config.mq_password}@{config.mq_url}:{config.mq_port}'
    exchange = config.mq_emergency_exchange
    queue = config.mq_emergency_queue
    listener = Listener(url=url, queue=queue, exchange=exchange, message_handler=message_handler)
  except KeyboardInterrupt:
    exit(0)