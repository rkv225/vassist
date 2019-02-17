import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def play_song(song, driver):
    # open a link in a new window
    actions = ActionChains(driver)
    about = driver.find_element_by_link_text('Web Speech API')
    actions.key_down(Keys.CONTROL).click(about).key_up(Keys.CONTROL).perform()
    driver.switch_to.window(driver.window_handles[-1])
    #driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+'t')
    driver.get('https://gaana.com/search/' + str(song))
    song_icon = driver.find_element_by_xpath("//*[@class='clearfix artworkload']/li[1]/div/div[2]/h3/a")
    #song_icon.click()
    song_icon.send_keys("\n")
    time.sleep(3)
    #driver.implicitly_wait(3)
    #driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + keys.TAB)
    driver.switch_to.window(driver.window_handles[0])

def stop_song(driver):
    driver.switch_to.window(driver.window_handles[-1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("stopping song")