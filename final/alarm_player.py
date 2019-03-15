import datetime
import json
import time
from firebase import firebase

class alarm_item:
    def __init__(self, id, h, m,ap):
        self.id=id
        self.hours=h
        self.minutes=m
        self.ap=ap

fb = firebase.FirebaseApplication('https://vassist-99157.firebaseio.com/', None)

print("Alarm Controller Running")

while(True):
    fetched_alarms=fb.get('/alarms', None)
    #getting the current time 
    current_time = datetime.datetime.now()
    #print (current_time.strftime("%I:%M:%S %p"))
    current_hour = int(current_time.strftime("%I"))
    current_minute = int(current_time.strftime("%M"))
    current_ap = 'a' if current_time.strftime("%p") == 'AM' else 'p'

    for key,val in fetched_alarms.items():
        print(key,val)
        obj=alarm_item(key,int(val['hours']),int(val['minutes']),val['ap'])
        if(obj.ap == current_ap):
            if(obj.hours == current_hour):
                if(obj.minutes == current_minute):
                    #delete the particular alarm entry from the firebase
                    fb.delete('/alarms', obj.id)
                    print("alarm ringing" + obj.id)

    print(".")
    time.sleep(30)