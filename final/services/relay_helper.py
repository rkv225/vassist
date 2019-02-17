from firebase import firebase
import os

fb = firebase.FirebaseApplication('https://vassist-99157.firebaseio.com/', None)

def get_state(sw):
    return fb.get('/switches/state/' + str(sw), None)

def get_switch(name):
    label1=fb.get('/switches/devices/1', None)
    label2=fb.get('/switches/devices/2', None)
    if(name == label1):
        return 1
    elif(name == label2):
        return 2
    else:
        return -1

def convert_to_binary(state):
    if(state == "on"):
        return 0
    else:
        return 1

def toggle(l_name, state):
    l_name = l_name.replace(' ','_')
    sw_no=get_switch(l_name)
    if(sw_no == -1):
        return "I can't find any device with this name"
    else:
        gpio_pin = 22 if sw_no == 1 else 27 
        cur_state=get_state(sw_no)
        if(cur_state == convert_to_binary(state)):
            if(cur_state == 0):
                return " Already in ON state"
            else:
                return " Already in OF state"
        else:
            st=convert_to_binary(state)
            l_name = l_name.replace('_',' ')
            os.system("gpio -g write " + str(gpio_pin) + " " + str(st))
            #modify the state in firebase
            fb.put('/switches/state',str(sw_no),str(st))
            if(st == 0):
                return str(l_name) + " Turned on successfully"
            else:
                return str(l_name) + " Turned off successfully"