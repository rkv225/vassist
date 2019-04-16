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

def change_state(sw_no, t_state):
    gpio_pin = 22 if sw_no == 1 else 27 
    st=t_state
    os.system("gpio -g write " + str(gpio_pin) + " " + str(st))
    #modify the state in firebase
    fb.put('/switches/state',str(sw_no),str(st))
    if(st == 0):
        return 1
    else:
        return 0

def toggle(l_name, state):
    l_name = l_name.replace(' ','_')
    sw_no = get_switch(l_name)
    t_state = convert_to_binary(state)
    if(sw_no == -1):
        return "I can't find any device with this name"
    else:
        cur_state=get_state(sw_no)
        if(cur_state == t_state):
            if(cur_state == 0):
                return " Already in ON state"
            else:
                return " Already in OF state"
        else:
            msg = change_state(sw_no, t_state)
            l_name = l_name.replace('_',' ')
            if(msg == 1):
                #turn on success
                return str(l_name) + " Turned on successfully"
            else:
                #turn off success
                return str(l_name) + " Turned off successfully"