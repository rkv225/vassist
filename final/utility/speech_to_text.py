#import speech_recognition as sr
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

def resetSTT(driver):
  driver.get("https://www.google.com/intl/en/chrome/demos/speech.html")
  s1= Select(driver.find_element_by_id("select_dialect"))
  s1.select_by_value('en-IN')

def operation(driver):
    print("Ask what you want me to do:")
    mic_button = driver.find_element_by_id("start_img")
    out_box = driver.find_element_by_id("final_span")
    mic_button.click()
    time.sleep(5)
    mic_button.click()
    out_text=out_box.text.lower()
    print(out_text)
    return out_text

def invoke(driver, hotword):
    print("Try saying "+str(hotword))
    mic_button = driver.find_element_by_id("start_img")
    out_box = driver.find_element_by_id("final_span")
    tries = 0
    while tries < 5:
        mic_button.click()
        time.sleep(4.5)
        mic_button.click()
        out_text=out_box.text.lower()
        print(out_text)
        tries = tries + 1
        if hotword in out_text:
            return True
        time.sleep(0.5)
    return False