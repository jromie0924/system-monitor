from tkinter import messagebox as mb, Tk

class UI():
  def __init__(self) -> None:
    pass

  def display_warning(self, t):
    root = Tk()
    root.withdraw()
    mb.showwarning('POWER LOSS DETECTED', f'URGENT: EMERGENCY SHUTDOWN IN {t} SECONDS.')
    root.destroy()

  def display_custom(self, title, message):
    root = Tk()
    root.withdraw()
    mb.showinfo(title, message)
    root.destroy()