# Importing Clock Class from Main.py
from Main import Clock

# Creating Clock App using Clock Class
if __name__ == '__main__':
    App = Clock()
    App.insertTimeLabel()
    App.updateTime()
    App.mainloop()