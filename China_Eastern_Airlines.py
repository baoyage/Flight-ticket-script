# China Eastern Airlines
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
week=['Wednesday','Wednesday','Wednesday','Wednesday','Wednesday','Wednesday'
      ,'Wednesday','Wednesday','Wednesday']
day=['2020-08-05','2020-08-12','2020-08-19'
     ,'2020-08-26','2020-09-02','2020-09-09','2020-09-16','2020-09-23','2020-09-30']





while (t!=9) :
    print("Current time: "+time.asctime( time.localtime(time.time()) )+"\n")
    a = Browser('chrome')
    try:
        a.visit('http://www.ceair.com/')
        alert = a.get_alert()
        alert.dismiss()    
    except:
        print("exception occured")
        a.quit()
        continue   


    try:    
        From = a.find_by_id('label_ID_0')
    except:
        print("exception occured")
        a.quit()
        continue
    try:
        From.click()
    except:
        print("exception occured")
        a.quit()
        continue
    active_web_element = a.driver.switch_to_active_element()
    i = 0
    time.sleep(1)
    while i!=3:
        active_web_element.send_keys(Keys.BACKSPACE)
        i+=1
    time.sleep(2)
    
    #FromBar=a.find_by_id('search_input')
    #FromBar.click()
    From.fill('纽约')
    time.sleep(2)
    To = a.find_by_id('label_ID_1')
    To.fill('上海')
    time.sleep(2)
    OneWay=a.find_by_id('ga_cn_jpdc')
    OneWay.click()
    time.sleep(2)
    Trip=a.find_by_id('depDt')
    Trip.click()
    time.sleep(2)
    pop=a.find_by_id('appd_wrap_close')
    pop.click()
    date=a.find_by_css('div[date="2020-08-01"]')
    date.click()
    Trip.click()
    finddatestr='div[date="'+day[t]+'"]'
    date=a.find_by_css(finddatestr)
    #  if (t==0):
    #     date=a.find_by_css('div[date="2020-08-05"]')
    # elif (t==1):
    #     date=a.find_by_css('div[date="2020-08-12"]')
    # elif (t==2):
    #     date=a.find_by_css('div[date="2020-08-19"]')
    # elif (t==3):
    #     date=a.find_by_css('div[date="2020-08-26"]')
    # elif (t==4):
    #     date=a.find_by_css('div[date="2020-09-02"]')
    # elif (t==5):
    #     date=a.find_by_css('div[date="2020-09-09"]')
    # elif (t==6):
    #     date=a.find_by_css('div[date="2020-09-16"]')
    # elif (t==7):
    #     date=a.find_by_css('div[date="2020-09-23"]')
    # elif (t==7):
    #     date=a.find_by_css('div[date="2020-09-30"]')


    time.sleep(1)
    date.click()
    try:
        Find_flights=a.find_by_id('btn_flight_search')
        Find_flights.click()
    except:
        print("exception occured")
        a.quit()
        continue
    time.sleep(20)
    a.windows.current=a.windows[1]
    Available=a.find_by_css('dl[class="head cols-3"]')
    try:
        AvailableDetails=Available.find_by_css('dd[data-type="economy"]')
    except:
        print("exception occured")
        a.quit()
        continue
    print(AvailableDetails.text)
    p=day[t]+'\nChina Eastern Airlines'
        

        
        
    if(AvailableDetails.text!="— —"):
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

    
    t+=1

    a.quit()
    time.sleep(20)
    if(t==9):
        t=0

   
    
input()


