import time
import datetime
import serial
      
ser = serial.Serial('/dev/ttyACM0', 9600)

now = datetime.datetime.now()
delay = 60-now.second
time.sleep(delay)

while True:
    message = ser.readline()
    now = datetime.datetime.now()
    nowstr = str(now)
    f=open("temperaturelog.txt","a")
    f.write(nowstr[0:19]+" "+str(message.decode('ascii')))
    f.close()
    now = datetime.datetime.now()
    delay = 60-now.second
    time.sleep(delay)

