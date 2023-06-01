import os, platform 
  
  
  
 try: 
  
  
  
         import requests 
  
  
  
 except: 
  
  
  
         os.system('pip2 install requests') 
  
  
  
  
  
  
  
 bit = platform.architecture()[0] 
  
  
  
 if bit == "64bit": 
  
         os.system('xdg-open https://www.facebook.com/Red.oupshack') 
  
  
  
         from file9 import Redoupshack 
  
  
  
         REDOUPSHACK_Main() 
  
  
  
  
  
  
  
 elif bit == "32bit": 
  
  
  
         os.system('xdg-open https://www.facebook.com/Red.oupshack') 
  
  
  
         os.system('python file9.py')