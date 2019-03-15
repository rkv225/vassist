import interfaces
from utility import text_to_speech
from utility import speech_to_text
import re

def think(speech_text, driver):
    
    def check_message(check):
        words_of_message = speech_text.split()
        if set(check).issubset(set(words_of_message)):
            return True
        else:
            return False
    
    if check_message(['who','are', 'you']):
        interfaces.who_are_you()
    
    elif check_message(['time']):
        interfaces.what_is_time()
    
    elif check_message(['of']):
        ir_match=re.match(r'(.+)\sof\s(.+)',speech_text)
        if ir_match:
            f_name = ir_match.group(1)
            r_name = ir_match.group(2)
            print(r_name)
            print(f_name)
            interfaces.ir_operation(r_name, f_name)
        else:
            interfaces.unknown_request()

    elif check_message(['turn']):
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

    elif check_message(['play']):
        music_match=re.match(r'play\s(.+)',speech_text)
        if music_match:
            query_text = music_match.group(1)
            interfaces.play_music(query_text, driver)
        else:
            interfaces.unknown_request()

    elif check_message(['alarm']):
        alarm_match=re.search(r'(\d{1,2}):(\d{1,2})\s([ap])',speech_text)
        if alarm_match:
            hours=alarm_match.group(1)
            minutes=alarm_match.group(2)
            ap=alarm_match.group(3)
            interfaces.set_alarm(hours, minutes, ap)
        else:
            interfaces.unknown_request()

    elif check_message(['wikipedia']):
        wiki_match=re.search(r'wikipedia about\s(.+)',speech_text)
        if wiki_match:
            input_text = wiki_match.group(1)
            interfaces.search_wiki(input_text)
        else:
            interfaces.unknown_request()
    
    elif check_message(['weather']):
        interfaces.get_weather()

    

    else:
        interfaces.unknown_request()