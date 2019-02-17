import interfaces
from utility import text_to_speech
from utility import speech_to_text


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
    
    elif check_message(['remote']):
        text_to_speech.operation('Say remote name')
        r_name = speech_to_text.operation(driver)
        print(r_name)
        text_to_speech.operation('Say function name')
        f_name = speech_to_text.operation(driver)
        print(f_name)
        interfaces.ir_operation(r_name, f_name)

    elif check_message(['switching']):
        text_to_speech.operation('Which device you want to operate')
        l_name = speech_to_text.operation(driver)#label name of the the device connected with the switches
        print(l_name)
        text_to_speech.operation('Do you want to turn on or off')
        state = speech_to_text.operation(driver)
        if(state == "of"):
            state="off"
        print(state)
        interfaces.relay_operation(l_name, state)

    else:
        interfaces.unknown_request()