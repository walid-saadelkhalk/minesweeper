import sys
import time
import keyboard 

def timer():
    for i in range(1000):
        sys.stdout.write( str(i).zfill(3) + '\r')
        sys.stdout.flush()
        if keyboard.is_pressed('space'):
            input('Paused, press enter to continue')
        time.sleep(1)
timer()


  





 