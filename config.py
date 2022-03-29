class Config():
  def __init__(self) -> None:
      self.mq_username=''
      self.mq_password=''
      self.mq_url='192.168.1.27'
      self.mq_port='5672'
      self.mq_emergency_exchange='Emergency'
      self.mq_emergency_queue='EmergencyCommands'