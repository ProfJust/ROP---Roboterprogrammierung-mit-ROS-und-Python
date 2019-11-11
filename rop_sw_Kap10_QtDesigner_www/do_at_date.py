# do_at_date.py
import datetime
import	time	
### JPG holen
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

import urllib
import psutil

print(" Speichert alle 15 Minuten ein Bild von der Webcam ")

while True:
    heute = datetime.date.today()
    now = datetime.datetime.now()
    nowstr = str(heute.day)+'.'+str(heute.month)+' '+str(now.hour)+':'+str(now.minute)
    print('  aktuelle Zeit: ' + nowstr)
    nochmin  = 15 - now.minute % 15
    print(' noch '+str(nochmin)+' Minuten bis zum naechsten Bild ')
    time.sleep(30)
  
    if(now.minute % 15 == 0):
        filestr = 'bild '+nowstr+'.jpg'
        website = urllib.urlopen('http://www.irs-alpsee-gruenten.de/se_data/_filebank/webcam/bbm.jpg')
        webfile = website.read()

        jpgfile = open(filestr, 'wb')
        jpgfile.write(webfile)
        print('---> speichere '+ filestr )

        website.close()
        jpgfile.close()
        
        #show Image
        img = Image.open(filestr)
        img.show()
        time.sleep(60)
        # img.close() funktioniert nicht, da separater Prozess
        # =>
        #https://stackoverflow.com/questions/6725099/how-can-i-close-an-image-shown-to-the-user-with-the-python-imaging-library
        # psutil can get the pid of the display process created by im.show() and 
        # kill the process with that pid on every operating system:
        for proc in psutil.process_iter():
            if proc.name() == "display":
                proc.kill()
        
