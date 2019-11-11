### sw05_Daten von Flask holen.py
###-------------------------------------------------
## Schreibt die Daten einer Webseite in eine Datei
###-------------------------------------------------
## vorher Server starten mit ..
## $sudo python sw03a_Text_Server_mit\ _Flask.py
###-------------------------------------------------

import urllib

website = urllib.urlopen("http://127.0.0.1")
datei = open("Flask.htm", "w")
zeilenStr = "irgendwas" 
zeilenNr = 0
while zeilenStr:
	zeilenNr = zeilenNr + 1
	zeilenStr = website.readline()
	datei.write(zeilenStr)
	if zeilenNr ==2:
		zahl = int(zeilenStr[0:20])
		print "Auf http://127.0.0.1 gelesene Zahl war "
		print zahl
website.close()
datei.close()
print("HTML-Daten in Datei Flask.htm geschrieben")
