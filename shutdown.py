import os
import time
import subprocess

class Shutdown_Controller:
  def __init__(self) -> None:
      pass
  
  def notify(self, title, message):
    userID = subprocess.run(['id', '-u', os.environ['SUDO_USER']],
      stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True).stdout.decode('utf-8').replace('\n', '')
    subprocess.run(['sudo', '-u', os.environ['SUDO_USER'], 'DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/{}/bus'.format(userID), 
      'notify-send', '-i', 'utilities-terminal', title, message],
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE,
      check=True)

  def countdown(self,t):
    # subprocess.Popen(['notify-send', f'URGENT: EMERGENCY COMPUTER SHUTDOWN IN {t} SECONDS.'])
    self.notify('POWER LOSS DETECTED', f'URGENT: EMERGENCY COMPUTER SHUTDOWN IN {t} SECONDS')
    while t:
      mins, secs = divmod(t, 60)
      timer = 'Automatic shutdown in: {:02d}:{:02d}'.format(mins, secs)
      print(timer, end='\r')
      time.sleep(1)
      t -= 1
    # subprocess.Popen(['notify-send', 'SIMULATE SHUTDOWN'])
    os.system("shutdown -P now")
