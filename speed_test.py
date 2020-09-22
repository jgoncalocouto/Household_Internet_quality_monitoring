import matplotlib.pyplot as plt
import time
import random
from collections import deque
import numpy as np
import speedtest
from datetime import datetime

time_list=[]
download_list=[]
ax = plt.axes(xlim=(0, 24), ylim=(0, 150))

line, = plt.plot(time_list,download_list,'r*')

plt.ion()
plt.ylim([0,150])
plt.show()
plt.xlabel('Time - [h]')
plt.ylabel('Download speed - [mb/s]')
now=datetime.now()
day=now.day
plt.title('Download Speed Meter - '+str(now.year)+'/'+str(now.month)+'/'+str(now.day))


try:
    while True:
        try:
            s = speedtest.Speedtest()
            s.get_best_server()
            dwn=s.download(threads=None)
        except:
            dwn=0
        download_list.append(dwn/(10**6))
        now=datetime.now()
        time_list.append(now.hour+now.minute/60+now.second/3600)
        line.set_xdata(time_list)
        line.set_ydata(download_list)
        plt.draw()
        plt.pause(60)
        print('Download Speed = '+str(dwn/(10**6))+' [mb/s]')
        #sleep(60)
except KeyboardInterrupt:
    print('Code execution stopped by user')
    
    
    
    
    
