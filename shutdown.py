import os
import time
from ui import UI

class Shutdown_Controller:
  def __init__(self) -> None:
      self._ui = UI()

  def countdown(self,t):
    # subprocess.Popen(['notify-send', f'URGENT: EMERGENCY COMPUTER SHUTDOWN IN {t} SECONDS.'])
    self._ui.display_warning(t)
    while t:
      mins, secs = divmod(t, 60)
      timer = 'Automatic shutdown in: {:02d}:{:02d}'.format(mins, secs)
      print(timer, end='\r')
      time.sleep(1)
      t -= 1
    # self._ui.display_custom("test", "simulate shutdown")
    os.system("shutdown -P now")
