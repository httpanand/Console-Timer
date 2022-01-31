import os
import time 

s = 0 
m = 0
h = 0

while True:
    os.system('cls')
    s = s+1
    counter = f'''
                {h}:{m}:{s}
    '''
    print(counter)
    time.sleep(1)
    if(s == 60):
        s = 0
        m = m +1
    if(m == 60):
        m = 0
        h = h+1


