import interfaces
from utility import text_to_speech
from utility import speech_to_text
import re
import sys
sys.path.append('NaiveBayes/')
from NaiveBayes import run_nb

'''
Id| Class
--|------------
1 | Relay
2 | IR
3 | Song
4 | Alarm
5 | Wikipedia
6 | Time
7 | Weather
8 | News
9 | Score
10| Introduction
11| For sequence model
'''

def think(speech_text, driver):
    
    def check_message(check):
        words_of_message = speech_text.split()
        if set(check).issubset(set(words_of_message)):
            return True
        else:
            return False

    command_type=run_nb.classify(speech_text)
    
    if command_type == 10:
        interfaces.who_are_you()
    
    elif command_type == 6:
        interfaces.what_is_time()
    
    elif command_type == 2:
        ir_match=re.match(r'(.+)\sof\s(.+)',speech_text)
        if ir_match:
            f_name = ir_match.group(1)
            r_name = ir_match.group(2)
            print(r_name)
            print(f_name)
            interfaces.ir_operation(r_name, f_name)
        else:
            interfaces.unknown_request()

    elif command_type == 1:
        relay_match=re.match(r'turn\s([a-z]+)\s(.+)',speech_text)
        if relay_match:
            state = relay_match.group(1)
            l_name = relay_match.group(2)
            print(l_name)
            if(state == "of"):
                state="off"
            print(state)
            interfaces.relay_operation(l_name, state)
        else:
            interfaces.unknown_request()

    elif command_type == 3:
        music_match=re.match(r'play\s(.+)',speech_text)
        if music_match:
            query_text = music_match.group(1)
            interfaces.play_music(query_text, driver)
        else:
            interfaces.unknown_request()

    elif command_type == 4:
        alarm_match=re.search(r'(\d{1,2}):(\d{1,2})\s([ap])',speech_text)
        if alarm_match:
            hours=alarm_match.group(1)
            minutes=alarm_match.group(2)
            ap=alarm_match.group(3)
            interfaces.set_alarm(hours, minutes, ap)
        else:
            interfaces.unknown_request()

    elif command_type == 5:
        wiki_match=re.search(r'wikipedia about\s(.+)',speech_text)
        if wiki_match:
            input_text = wiki_match.group(1)
            interfaces.search_wiki(input_text)
        else:
            interfaces.unknown_request()
    
    elif command_type == 7:
        interfaces.get_weather()

    elif command_type == 8:
        news_match = re.search(r'(finance|business|world|globe|global|tech|sports)', speech_text)
        category = "default"
        if news_match:
            category = news_match.group(1)
        interfaces.get_req_news(category)    
    
    elif command_type == 11:
        #for sequence model
        interfaces.unknown_request()#replace with the code of seq model

    else:
        interfaces.unknown_request()