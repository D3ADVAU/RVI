#coding=utf-8
#!/usr/bin/env python3
#SCRIPT KIDDIES NOT ALLOWED
#IF YOU COPY THIS SCRIPT PLEASE GIVE THE CREDIT TO @D3ADVAU
#D3ADVAU
##IMOORTING MODULES##
import os,sys,socket,time
try:
   import requests
   from requests.structures import CaseInsensitiveDict
except:
      os.system("pip install requests")
import requests
from requests.structures import CaseInsensitiveDict
##LOGO##
logo = """\n            \x1b[1;92m/$$$$$$$  \x1b[1;93m/$$    /$$ \x1b[1;92m/$$$$$$\n           | $$__  $$\x1b[1;93m| $$   | $$\x1b[1;92m|_  $$_/\n           | $$  \ $$\x1b[1;93m| $$   | $$\x1b[1;92m  | $$\n           | $$$$$$$/\x1b[1;93m|  $$ / $$/\x1b[1;92m  | $$\n           | $$__  $$\x1b[1;93m \  $$ $$/ \x1b[1;92m  | $$\n           | $$  \ $$\x1b[1;93m  \  $$$/  \x1b[1;92m  | $$\n           | $$  | $$\x1b[1;93m   \  $/   \x1b[1;92m /$$$$$$\n           |__/  |__/\x1b[1;93m    \_/    \x1b[1;92m|______/\n\n        \x1b[1;93mWEBSITES REVERSE IP ADDRESS FINDER\n\n    \x1b[1;96m╔══════════════════════════════════════════╗\n    ║\x1b[1;92m  Author\x1b[1;93m     :     Dead-Man | D3ADVAU    \x1b[1;96m ║\n    ║\x1b[1;92m  Github \x1b[1;93m    :     github.com/D3ADVAU    \x1b[1;96m ║\n    ║\x1b[1;92m  Facebook \x1b[1;93m  :       fb.com/D3ADVAU      \x1b[1;96m ║\n    ╚══════════════════════════════════════════╝"""
###RVI###
def rvi():
    os.system("clear")
    print (logo)
    file = input("\n\x1b[1;94m   WEBSITES TXT FILE NAME: \x1b[1;95m")
    if ".txt" in file:
      try:
          file = open(file).read().split()
      except:
          print ("\x1b[1;91mFILE PATH UNKNOWN PLEASE COPY YOUR FILE TO THIS FOLDER ")
          os.sys.exit()
    else:
        print ("\x1b[1;91mONLY ALLOWED .txt FILE")
        os.sys.exit()
    sfile = input("\n\x1b[1;94m  ENTER FILE NAME TO SAVE REVERSE: \x1b[1;95m")
    for url in file:
               url=url.replace("https://", "").replace(" ","").replace("/", "").replace("www.","")
               url= socket.gethostbyname(url)
               rurl = "https://sonar.omnisint.io/reverse/"+str(url)
               headers = CaseInsensitiveDict()
               headers["Content-Type"] = "application/x-www-form-urlencoded"
               resp = requests.get(rurl, headers=headers)
               data = resp.json()
               for data in data:
                       with open(sfile, "a") as file:
                                                    file.write(str(data)+"\n")
                       print ("\x1b[1;92m  SUCCESS \x1b[1;96m"+str(data)+"\x1b[1;92m SAVED IN \x1b[1;93m"+str(sfile))
                       time.sleep(.5)
###MAIN###
def main():
         os.system("clear")
         print (logo)
         print ("\n\x1b[1;91m  [\x1b[1;93m01\x1b[1;91m]\x1b[1;92mSTART TOOL\n\n\x1b[1;91m  [\x1b[1;93m02\x1b[1;91m]\x1b[1;92mCONTACT DEVOLOPER\n\n\x1b[1;91m  [\x1b[1;93m00\x1b[1;91m]\x1b[1;92mEXIT")
         chooseOption = input("\n\x1b[1;92m CHOOSE AN OPTION:\x1b[1;93m ")
         if chooseOption == "1" or chooseOption == "01":
            os.system("clear")
            rvi()
         if chooseOption == "00" or chooseOption == "0":
            os.system("clear")
            print (logo)
            os.sys.exit()
         if chooseOption == "02" or chooseOption == "2":
            os.system("xdg-open https://facebook.com/D3ADVAU")
            main()
         else:
             print ("  \x1b[1;91mWRONG OPTION CHOOSEN PLEASE ENTER  A CORRECT OPTION")
             main()
if __name__ == "__main__":
    main()
