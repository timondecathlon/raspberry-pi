#!/usr/bin/env python
# -*- coding: utf-8 -*-
#project: home-smart-home.ru
#подключаем сигнальный провод на 16 pin BCM
import time
import RPi.GPIO as GPIO

import urllib.request

#print("Content-type: text/html")
 
def RCtime (RCpin):
        GPIO.setmode(GPIO.BCM)     
        GPIO.setup(RCpin, GPIO.IN)      
#       GPIO.wait_for_edge(RCpin,GPIO.FALLING)  #можно расскомментить один из 3-х вариантов
        GPIO.wait_for_edge(RCpin,GPIO.RISING)
#       GPIO.wait_for_edge(RCpin,GPIO.BOTH)
        signal = GPIO.input(RCpin)   
        print ("обнаружено движение")
        
        webUrl  = urllib.request.urlopen('https://ironlinks.ru/penny/test.php')
         
        
        #text = "обнаружено движение..." 
        #print(text, end='', flush=True)
        #time.sleep(3)
        #print('\b' * len(text) + ' ' * len(text), end='', flush=True)
        
while True:
        RCtime(16)
        time.sleep(5)
        
