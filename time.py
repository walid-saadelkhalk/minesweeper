import sys
import time

def decompte():
    for i in range(1000):
        sys.stdout.write( str(i).zfill(3) + '\r')
        sys.stdout.flush()
        time.sleep(1)
decompte()


