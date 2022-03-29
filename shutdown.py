import os
import time

def countdown(t):
  while t:
    mins, secs = divmod(t, 60)
    timer = 'Automatic shutdown in: {:02d}:{:02d}'.format(mins, secs)
    print(timer, end='\r')
    time.sleep(1)
    t -= 1
  os.system("shutdown -P now")

if __name__ == '__main__':
  try:
    t = 30
    countdown(t)
  except KeyboardInterrupt:
    exit(0)
