from utility import text_to_speech as tts
from utility import speech_to_text
from services import introduce
from services import time_tell
from services import ir_helper
from services import relay_helper
from services import music
from services import alarm_helper
from services import wiki_helper
from services import weather_helper
import time

def who_are_you():
    text = introduce.intro()
    tts.operation(text)
    
def what_is_time():
    text = time_tell.tell()
    tts.operation(text)

def play_music(query_text, driver):
    tts.operation('playing song')
    music.play_song(query_text, driver)
    #check stop command
    while True:
        speech_to_text.resetSTT(driver)
        if speech_to_text.invoke(driver, 'stop'):
            #user said stop
            music.stop_song(driver)
            return
        else:
            #user did not said stop in n tries
            speech_to_text.resetSTT(driver)

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

def set_alarm(hours, minutes, ap):
    response = alarm_helper.create(hours, minutes, ap)
    tts.operation(response)

def search_wiki(input_text):
    tts.operation('searching')
    response = wiki_helper.search(input_text)
    tts.operation(response)

def get_weather():
    tts.operation('getting weather')
    response = weather_helper.get_report()
    tts.operation(response)
    
def unknown_request():
    tts.operation("Sorry I don't know this.")