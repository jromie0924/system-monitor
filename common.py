import pika
from pika.adapters.blocking_connection import BlockingChannel, BlockingConnection
import time


class Common():
  def __init__(self) -> None:
      pass

  def open_connection(self, url):
    while True:
      try:
        return pika.BlockingConnection(parameters=pika.URLParameters(url))
      except:
        print("Cannot connect to RabbitMQ server.")
        time.sleep(5)
