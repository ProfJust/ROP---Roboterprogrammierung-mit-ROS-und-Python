# date_and_time.py
import datetime
import	time	

# Ein Objekt mit vorgegeben Datum instanzieren
myday = datetime.date(1995,1,22)
print(myday.day,myday.month, myday.year)

# Ein Objekt mit aktuellem Datum instanzieren
heute = datetime.date.today()
print(heute)

# Addition von Tagen 
morgen = heute + datetime.timedelta(1)
print(morgen)

# Bestimmung von Zeitraeumen in Tagen 
begin_ss = datetime.date(2019,3,1)
print("Der Semesterrest in Tagen:")
rest = begin_ss - heute
print(rest)

# Ein Objekt fuer die Uhrzeit
now = datetime.datetime.now()
print(now)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond) #Systemzeit nicht Uhrzeit

# nochmal - wie lange dauert dass? 
now = datetime.datetime.now()
print(now)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond) 

# Messung eine Zeit
print("Warte 5 sec")
time.sleep(5)
# Beim Aufruf von sleep() nimmt das Betriebssystem den Prozess aus der Menge der
# laufenden	Prozesse	heraus	und	steckt	ihn	in	eine	Warteschlange.	

now = datetime.datetime.now()
print(now)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)