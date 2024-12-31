import datetime
import time
Age = 0
while True :
  print(Age)
  Age += 1
  
  date_actuelle = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
  if date_actuelle <= 12:
    print("Good morning")
  elif date_actuelle >=  12 :
    print("Good afternoon")
    
  print(date_actuelle)
  time.sleep(60)