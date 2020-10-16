# Delta Airlines
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

account_sid = 'AC9b4320156d17f7c767783513a50372a5'
auth_token = 'db828565d06634def807b81cb78b9b78'
client = Client(account_sid, auth_token)
success=0

t=0
week=['Thursday','Thursday','Thursday','Thursday','Thursday'
    ,'Thursday','Thursday','Thursday',
    'Friday' ,'Friday','Friday','Friday','Friday'
    ,'Friday','Friday','Friday','Friday']

day=['6 August 2020','13 August 2020','20 August 2020'
     ,'27 August 2020','3 September 2020','10 September 2020',
     '17 September 2020','24 September 2020',
     
     '31 July 2020','7 August 2020','14 August 2020'
     ,'21 August 2020','28 August 2020','4 September 2020'
     ,'11 September 2020','18 September 2020','25 September 2020'
     ]

while (t!=15) :
    print("Current time: "+time.asctime( time.localtime(time.time()) )+"\n")
    a = Browser('chrome')
    a.driver.set_window_size(640, 1480)

    try:
        a.visit('https://www.delta.com/')
    except:
        print('exception occured')
        a.quit()
        continue

    Open=a.find_by_id('mobile-expand-widg')
    Open.click()

    From = a.find_by_id('fromAirportName')
    From.click()
    FromBar=a.find_by_id('search_input')
    FromBar.click()
    
    active_web_element = a.driver.switch_to_active_element()

    i = 0
    time.sleep(1)
    while i!=3:
        active_web_element.send_keys(Keys.BACKSPACE)
        i+=1
    time.sleep(1)
    if t<8 :
        FromBar.fill('SEA')
    else:
        FromBar.fill('DTW')
    time.sleep(1)
    Close=a.find_by_css('button[class="float-right close"]')
    Close.click()

    To = a.find_by_id('toAirportName')
    To.click()
    ToBar=a.find_by_id('search_input')
    ToBar.click()
    time.sleep(1)
    ToBar.fill('PVG')
    time.sleep(1)
    Close=a.find_by_css('button[class="float-right close"]')
    Close.click()

    Trip=a.find_by_css('span[class="select-ui-wrapper "]')
    Trip.click()

    time.sleep(3)

    OneWay=a.find_by_id('ui-list-selectTripType1')
    OneWay.click()
    Date=a.find_by_css('div[class="calDispValueCont icon-Calendar  "]')
    Date.click()
    datestr='a[aria-label="'+day[t]+', '+week[t]+'"]'
    date=a.find_by_css(datestr)
    # if(t==0):    
    #     date=a.find_by_css('a[aria-label="30 July 2020, Thursday"]')
    # elif (t==1):
    #     date=a.find_by_css('a[aria-label="6 August 2020, Thursday"]')
    # elif (t==2):
    #     date=a.find_by_css('a[aria-label="13 August 2020, Thursday"]')
    # elif (t==3):
    #     date=a.find_by_css('a[aria-label="20 August 2020, Thursday"]')
    # elif (t==4):
    #     date=a.find_by_css('a[aria-label="27 August 2020, Thursday"]')
    # elif (t==5):
    #     date=a.find_by_css('a[aria-label="31 July 2020, Friday"]')
    # elif (t==6):
    #     date=a.find_by_css('a[aria-label="7 August 2020, Friday"]')
    # elif (t==7):
    #     date=a.find_by_css('a[aria-label="14 August 2020, Friday"]')
    # elif (t==8):
    #     date=a.find_by_css('a[aria-label="21 August 2020, Friday"]')
    # elif (t==9):
    #     date=a.find_by_css('a[aria-label="28 August 2020, Friday"]')
        
    date.click()
    Select=a.find_by_css('button[class="donebutton"]')
    Select.click()
    Find_flights=a.find_by_id('btn-book-submit')
    try:
        
        Find_flights.click()
    except:
        print('exception occured')
        a.quit()
        continue

        
    time.sleep(10)
    try:
        During_time=a.find_by_css('span[class="ng-star-inserted"]')
    except:
        print('exception occured')
        a.quit()
        continue        
    p=day[t]+', ' +week[t]+'\nDelta Airlines'
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
                from_='+15714140158',
                to='+13154801605')
            print(message.sid)
        else:
            print(p)
            print("fail")

    else:
        print(p)
        print("fail")

    t+=1

    a.quit()
    time.sleep(40)
    if(t==15):
        t=0

    
input()


