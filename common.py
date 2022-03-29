import pika
from pika.adapters.blocking_connection import BlockingChannel, BlockingConnection


class Common():
  def __init__(self) -> None:
      pass

  def open_connection(self, url):
    return pika.BlockingConnection(parameters=pika.URLParameters(url))