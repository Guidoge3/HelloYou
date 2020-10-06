import datetime
import time


a = True

while a == True:
    x = datetime.datetime.now()
    print ( x.strftime("%c"))
    time.sleep ( 2 )
    print ("Hallo! Mijn naam is Guido")
    time.sleep ( 1 )
    print ("Wat is jouw naam?")
    time.sleep ( 0.5 )
    n = input("Enter Username:")
    time.sleep ( 1 )
    print ("Hallo, " + n + " leuk je te ontmoeten!")
    C = input("Wil je verdergaan?:")
    if C == "yes":
        continue 
    else:
        print ("Het programma wordt afgesloten, C ya next time!")
        break