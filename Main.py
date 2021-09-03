# Importing tkinter and datetime Modules
from tkinter import *
import datetime

# Creating Clock Class
class Clock(Tk):

    def __init__(self):
        """ Takes Methods From Tk Class of Tkinter Module """
        super().__init__()
        self.geometry('500x150+750+250')
        self.minsize(430, 60)
        self.title('Clock App')
        self.config(bg='#10111b')

    def insertTimeLabel(self):
        """ Adds Time Label in App """
        self.timeLabel = Label(self, text=datetime.datetime.now().strftime('%I:%M:%S:%f')[:11]+datetime.datetime.now().strftime(' %p'), font=('Consolas', 40, 'bold'), bg='#10111b', fg='#53acb0', bd=0)
        self.timeLabel.pack(anchor=CENTER, expand=YES, fill=BOTH, padx=10, pady=10)

    def updateTime(self):
        """ Update Time in App after every 1 milisecond"""
        self.timeLabel.config(text=datetime.datetime.now().strftime('%I:%M:%S:%f')[:11]+datetime.datetime.now().strftime(' %p'))
        self.after(1, self.updateTime)

if __name__ == '__main__':
    print('Please Run \'Clock.py\'\n')
    input()