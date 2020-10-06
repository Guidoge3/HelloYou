import time
import datetime

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
    time.sleep ( 1 )
    print ("ik heb 3 leuke vragen voor jou over mij!")
    time.sleep ( 1 )
    antwoord1 = input("ik kom uit \n A Nieuw-Vennep \n B Haarlem \n C Hoorn \n antwoord: ")
    if ( antwoord1 == "A"):
        print("geweldig! dat is goed")
    elif ( antwoord1 == "B"):
        print("helaas dat is fout")
    elif ( antwoord1 == "C"):
        print("helaas dat is fout")
    print ("nice! hier komt vraag 2!")
    time.sleep ( 1 )
    antwoord2 = input ("mijn grootste hobby is \n A Netflixen \n B Gamen \n C Tekenen \n antwoord: ")
    if ( antwoord2 == "A"):
        print("helaas dat is fout")
    elif ( antwoord2 == "B"):
        print("Ja! goed geraden")
    elif (antwoord2 == "C"):
        print("helaas dat is fout")
        time.sleep ( 1 )
    print ("hier komt de laatste vraag!")
    time.sleep ( 1 )
    antwoord3 = input("mijn favoriete eten is \n A Carpaccio \n B Pizza \n C Patat \n antwoord: ")
    if ( antwoord3 == "A"):
        print ("inderdaad! dat klopt helemaal")
    elif ( antwoord3 == "B"):
        print ("helaas dat is fout maar pizza is wel heel erg lekker ;)")
    elif ( antwoord3 == "C"):
        print ("helaas dat is fout")
    time.sleep ( 2 )
    print("je hebt de vragen goed beantwoord!")
    time.sleep ( 1 )
    print("ik geef je even een aantal secondes om bij te komen van deze moeilijke vragen")
    time.sleep ( 5 )
    break 
    
