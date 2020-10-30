import time


Vluchteling = ("Wahhab")


def vraagA():
    print("A = Iran / B = Syrië")
    while True:
        antw = input()
        if antw == "A":
            print("Ja klopt! ik kom inderdaad uit Iran")
            vraagAA()
            break
        elif antw == "B":
            print("Nee. daar kom ik niet vandaan")
            vraagAB()            
            break
        else:
            print("ik snap je antwoord niet. Vul een geldig antwoord in: ")
            vraagA()
 

def vraagAA():
    print("Naar welke stad ben ik gevlucht?")
    print("A = Amsterdam / B = Berlijn")
    while True:
        antw = input()
        if antw == "A":
            print("nou laten we dan daar maar heen gaan")
            vraagAAA()
            break
        elif antw == "B":
            print("oke dan dan gaan we naar Berlijn")
            vraagAAB()            
            break
        else:
            print("ik snap je antwoord niet. Vul een geldig antwoord in: ")
            vraagAA()


def vraagAB():
    print("Wil je mijn levensverhaal horen van hoe ik hier terecht ben gekomen?")
    print("A = Ja graag! / B = Nee dankje")
    while True:
        antw = input()
        if antw == "A":
            print("Leuk! ik zal je mijn levensverhaal vertellen.")
            vraagAAA()
            break
        elif antw == "B":
            print("Oke dan niet. Dag!")
            vraagAAB()            
            break
        else:
            print("ik snap je antwoord niet. Vul een geldig antwoord in: ")
            vraagAB()

#=======================================================================================

print("Hallo mijn naam is ", Vluchteling, " waar denk je dat ik vandaan kom?")

vraagA()
