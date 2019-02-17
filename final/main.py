import json
from utility import text_to_speech
from utility import speech_to_text
from brain import think
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from firebase import firebase

#firebase database
fb = firebase.FirebaseApplication('https://vassist-99157.firebaseio.com/', None)

#init Relays
os.system("gpio -g mode 22 output")#for sw1
os.system("gpio -g mode 27 output")#for sw2
os.system("gpio -g write 22 1")
os.system("gpio -g write 27 1")
fb.put('/switches/state',"1",1)
fb.put('/switches/state',"2",1)

#init LIRC if needed

#selenium init and setup
chrome_options = Options()
chrome_options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_popups": 1,
    "profile.managed_default_content_settings.images": 2
  })
driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver", chrome_options=chrome_options)

def main():
  text_to_speech.operation('Hello There! Wait for a while to let me set things up.')
  #get profile data from firebase
  profile=fb.get('/profile',None)
  #initialize STT for the first time
  speech_to_text.resetSTT(driver)
  #welcome message
  text_to_speech.operation('Hello ' + profile['name'] + '. How can I help you?')
  while True:
    if speech_to_text.invoke(driver, 'listen'):
      #user said listen
      text_to_speech.operation('Yes, say it')
      rec_text = speech_to_text.operation(driver)
      think(rec_text, driver)
    else:
      #user did not said listen in n tries
      speech_to_text.resetSTT(driver)

#opening
main()