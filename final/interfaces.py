from utility import text_to_speech as tts
from services import introduce
from services import time
from services import ir_helper
from services import relay_helper

def who_are_you():
    text = introduce.intro()
    tts.operation(text)
    
def what_is_time():
    text = time.tell()
    tts.operation(text)

def ir_operation(r_name, f_name):
    f_name=f_name.replace(' ','_')
    print(f_name)
    key=ir_helper.get_key(r_name, f_name)
    if(not key):
        tts.operation("Either Device or function is incorrect")
    else:
        print(key)
        ir_helper.send_code(r_name, key)
        tts.operation("Command send to " + r_name)

def relay_operation(l_name, state):
    response = relay_helper.toggle(l_name, state)
    tts.operation(response)
    
def unknown_request():
    tts.operation("Sorry I don't know this.")