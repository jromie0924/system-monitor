import os
import time
from publisher import Publisher
from config import Config

class Network():
  def __init__(self) -> None:
    config = Config()
    url = f'amqp://{config.mq_username}:{config.mq_password}@{config.mq_url}:{config.mq_port}'
    self._publisher = Publisher(url, config.mq_emergency_exchange, config.mq_emergency_queue)

  def ping(self):
    hostname = '192.168.1.1'
    response = os.system(f'ping -c 1 {hostname}')
    if response == 0:
      print('Network up')
      return True
    print ('Network down')
    return False
  
  def publish_command(self):
    self._publisher.publish_message('SHUTDOWN')

if __name__ == '__main__':
  network = Network()
  try:
    while True:
      result = network.ping()
      if not result:
        network.publish_command()
      time.sleep(60)
  except KeyboardInterrupt:
    exit(0)