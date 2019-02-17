import os
import json
from firebase import firebase

class Remote:
    name=""
    count=0
    buttons={}

#ir pins are gpio_in_pin=18 gpio_out_pin=17

def add_new_remote():
    fb = firebase.FirebaseApplication('https://vassist-99157.firebaseio.com/', None)
    rr=Remote()
    rr.count=int(input('Enter the number of buttons:'))
    rr.name=str(raw_input('Enter the name of Remote:'))
    for i in range(1, rr.count+1):
        # rr.buttons['KEY_' + str(i)]=raw_input('Label for KEY_'+ str(i))
        button_label=raw_input('Label for KEY_'+ str(i))
        rr.buttons[button_label]='KEY_' + str(i)
    json_data=json.dumps(rr.buttons)
    json_data=json.loads(json_data)
    for a,b in rr.buttons.items():
        print(b + "is labelled" + a)
    os.system("sudo /etc/init.d/lircd stop")
    os.system("sudo irrecord -d /dev/lirc0 ~/lircd.conf")
    os.system("sudo cat " + rr.name + ".lircd.conf " + "/etc/lirc/lircd.conf > tmp.lircd.conf")
    os.system("sudo mv tmp.lircd.conf /etc/lirc/lircd.conf")
    fb.put('remotes', rr.name, json_data)

def display_remotes():
    fb = firebase.FirebaseApplication('https://vassist-99157.firebaseio.com/', None)
    result=fb.get('/remotes',None)
    print(result)
   

add_new_remote()