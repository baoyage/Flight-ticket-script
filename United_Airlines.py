
# United Airlines
from splinter import Browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from time import sleep
import traceback
import time, sys
import codecs
import argparse
import os
import time
from twilio.rest import Client

account_sid = 'AC26336efaed341e48c8aebe93d54b1fcf'
auth_token = '4838133b770462b2d61e30faf7902ec8'
client = Client(account_sid, auth_token)
success=0

t=0
week=['Wednesday','Saturday','Wednesday','Saturday','Wednesday'
      ,'Saturday','Wednesday','Saturday','Wednesday']
day=['September 2','September 5','September 9','September 12'
     ,'September 16','September 19','September 23','September 26'
     ,'September 30']
while (t!=9) :
    print("Current time: "+time.asctime( time.localtime(time.time()) )+"\n")
    a = Browser('chrome')
    a.driver.set_window_size(940, 980)
    a.visit('https://www.united.com/en/us')



    From = a.find_by_id('bookFlightOriginInput')
    try:
        From.click()
    except:
        print("exception occured")
        a.quit()
        continue

    active_web_element = a.driver.switch_to_active_element()

    i = 0
    time.sleep(1)
    while i!=20:
        active_web_element.send_keys(Keys.BACKSPACE)
        i+=1
    From = a.find_by_id('bookFlightOriginInput')
    From.click()

    active_web_element = a.driver.switch_to_active_element()

    i = 0
    time.sleep(1)
    while i!=20:
        active_web_element.send_keys(Keys.BACKSPACE)
        i+=1
    From.fill('San Francisco, CA, US (SFO)')
    time.sleep(1)
    Close=a.find_by_css('button[class="app-components-AutoComplete-Legacy-styles__closeButton--1bI2u"]')
    Close.click()
    time.sleep(1)
    To = a.find_by_id('bookFlightDestinationInput')
    To.fill('Shanghai (PVG)')
    time.sleep(1)
    Close=a.find_by_css('button[class="app-components-AutoComplete-Legacy-styles__closeButton--1bI2u"]')
    Close.click()
    time.sleep(1)
    Oneway=a.find_by_id('oneway')
    Oneway.click()
    time.sleep(1)
    DepartDate=a.find_by_name('DepartDate')
    DepartDate.click()
    time.sleep(1)
    #Backdate=a.find_by_css('button[class="DayPickerNavigation_button DayPickerNavigation_button_1 DayPickerNavigation_button__horizontal DayPickerNavigation_button__horizontal_2 DayPickerNavigation_leftButton__horizontal DayPickerNavigation_leftButton__horizontal_3"]')
    #Backdate.click()
    time.sleep(1)
    datestr='td[aria-label="'+week[t]+', '+day[t]+', 2020"]'
    date=a.find_by_css(datestr)
    # if(t==0):    
    #     date=a.find_by_css('td[aria-label="Wednesday, September 2, 2020"]')
    # elif (t==1):
    #     date=a.find_by_css('td[aria-label="Saturday, September 5, 2020"]')
    # elif (t==2):
    #     date=a.find_by_css('td[aria-label="Wednesday, September 9, 2020"]')
    # elif (t==3):
    #     date=a.find_by_css('td[aria-label="Saturday, September 12, 2020"]')
    # elif (t==4):
    #     date=a.find_by_css('td[aria-label="Wednesday, September 16, 2020"]')
    # elif (t==5):
    #     date=a.find_by_css('td[aria-label="Saturday, September 19, 2020"]')
    # elif (t==6):
    #     date=a.find_by_css('td[aria-label="Wednesday, September 23, 2020"]')
    # elif (t==7):
    #     date=a.find_by_css('td[aria-label="Saturday, September 26, 2020"]')
    # elif (t==8):
    #     date=a.find_by_css('td[aria-label="Wednesday, September 30, 2020"]')
    #date=a.find_by_css('td[aria-label="Tuesday, September 1, 2020"]')
    date.click()
    time.sleep(1)
    Find_flights=a.find_by_css('button[aria-label="Find flights"]')
    Find_flights.click()
    time.sleep(5)
    try:
        During_time=a.find_by_css('a[class="flight-duration otp-tooltip-trigger"]')
    except:
        print("exception occured")
        a.quit()
        continue    
    time.sleep(5)
    
    p=week[t]+', '+day[t]+', 2020 \nUnited Airlines'
 
    time.sleep(1)
    if (During_time.is_empty()!=True):
        print(During_time.text)
        hourstr=During_time.text[0:2]
        hour=int(hourstr)
       
        if(hour<16):
            print(p)
            print("success")
            success=1
            
            message = client.messages \
            .create(
                body=p+', success',
                from_='+15109535080',
                to='+13154801605')
            print(message.sid)
        else:
            print(p)
            print("fail")
            
    else:
        print(p)
       

    t+=1
    a.quit()
    time.sleep(60)
    if(t==9):
        t=0


#active_web_element = a.driver.switch_to_active_element()
#i=0
#while i!=10:
#    active_web_element.send_keys(Keys.BACKSPACE)
#    i+=1
#DepartDate.fill('Aug 01')

#if b.is_text_present('splinter.readthedocs.io'):
#    print ("Yes, found it! :")
#else:
#    print ("No, didn't find it :")
input()

#<td class="CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2" role="button" aria-label="Monday, August 31, 2020" tabindex="-1" style="width: 39px; height: 38px;">31</td>
