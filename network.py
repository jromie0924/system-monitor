import os
import time
from publisher import Publisher
from config import Config

class Network():
  def __init__(self) -> None:
    config = Config()
    url = f'amqp://{config.mq_username}:{config.mq_password}@{config.mq_url}:{config.mq_port}'
    success = False
    while not success:
      try:
        self._publisher = Publisher(url, config.mq_emergency_exchange, config.mq_emergency_queue)
        success = True
      except:
        print("Cannot connect ot RabbitMQ server.")
        time.sleep(5)

  def ping(self):
    hostname = '192.168.1.1'
    response = os.system(f'ping -c 1 {hostname}')
    if response == 0:
      print('Network up')
      return True
    print ('Network down')
    return False
  
  def publish_command(self):
    retval = True
    try:
      self._publisher.publish_message('SHUTDOWN')
    except:
      print("Cannot connect to RabbitMQ server.")
      retval = False
    return retval

if __name__ == '__main__':
  network = Network()
  try:
    while True:
      result = network.ping()
      if not result:
        result = network.publish_command()
        if not result:
          del network
          network = Network()
      time.sleep(10)
  except KeyboardInterrupt:
    exit(0)