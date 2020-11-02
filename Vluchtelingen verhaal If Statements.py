import time


Vluchteling = ("Wahhab")


def vraag1():
    print("A = Iran / B = Syrië")
    while True:
        antw = input()
        if antw == "A":
            print("Ja klopt! ik kom inderdaad uit Iran")
            vraag2()
            break
        elif antw == "B":
            print("Nee. daar kom ik niet vandaan. Hoe kan je dat niet weten? ga maar weg ook.")
            break
        else:
            print("ik snap je antwoord niet. Vul een geldig antwoord in: ")
            vraag1()


def vraag2():
    print("\nik hoorde op de radio dat er een oorlog kwam wat deed ik?")
    print("A = niets en je dacht dat het een oefening was / B = je probeerde te vluchten en kreeg daar problemen mee en je zit nu vast")
    while True:
        antw = input()
        if antw == "A":
            print("Na een tijd wachten hoorde je schoten en wilde weg.")
            vraag3()
            break
        elif antw == "B":
            print("Je zit vast. jammer dan")
            break
        else:
            print("ik snap je antwoord niet. Vul een geldig antwoord in: ")
            vraag2()


def vraag3():
    print("\nin mijn land zag ik bom vallen en er waren schoten wat deed ik?")
    print("A = Gewonden helpen / B = Vluchten")
    while True:
        antw = input()
        if antw == "A":
            print("Ik werd geraakt door een kogel toen ik gewonden wilde helpen")
            break
        elif antw == "B":
            print("Ik vluchtte de stad uit")
            vraag4()
            break
        else:
            print("ik snap je antwoord niet. Vul een geldig antwoord in: ")
            vraag3()


def vraag4():
    print("\nonderweg zag ik mensen van het vijandige leger naar ons toe komen wat deed ik?")
    print("A = ik verstop me / B = ik ren zo hard mogelijk weg")
    while True:
        antw = input()
        if antw == "A":
            print("ik probeerde te verstoppen maar ik werd gevonden en word nu meegenomen.")
            vraag5()
            break
        elif antw == "B":
            print("ik begon te rennen en gelukkig ben ik niet gezien ik ben aan de vijand ontsnapt.")
            vraag6()
            break
        else:
            print("ik snap je antwoord niet. Vul een geldig antwoord in: ")
            vraag4()


def vraag5():
    print("\nik ben meegenomen naar een werkkamp waar ik geen vrijheid had ik probeerde er iets aan te doen.")
    print("A = ik probeerde te ontsnappen / B = ik probeerde terug te vechten")
    while True:
        antw = input()
        if antw == "A":
            print("ik werd gesnapt en opgesloten tot executie")
            vraag7()
            break
        elif antw == "B":
            print("ik probeerde het leger van het kamp te doden maar dat werd mijn eigen dood.")
            break
        else:
            print("ik snap je antwoord niet. Vul een geldig antwoord in: ")
            vraag5()


def vraag6():
    print("\nJe bent ontsnapt aan de oorlog wat ga je doen?")
    print("A = mensen zoeken / B = naar een bekende veilige plek gaan")
    while True:
        antw = input()
        if antw == "A":
            print("je zoekt vrienden en familie en daarmee ga je samen schuilen.")
            vraag8()
            break
        elif antw == "B":
            print("je vlucht naar het buitenland zonder familie of vrienden en zoekt een veilige plek op.")
            vraag9()
            break
        else:
            print("ik snap je antwoord niet. Vul een geldig antwoord in: ")
            vraag6()


def vraag7():
    print("\nJe mag je eigen dood kiezen, kies maar:")
    print("A = onthoofding / B = levend verbrand worden")
    while True:
        antw = input()
        if antw == "A":
            print("ughghggudgdkbvkd... dood")
            break
        elif antw == "B":
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA het braaaand!!!.... dood")
            break
        else:
            print("ik snap je antwoord niet. Vul een geldig antwoord in: ")
            vraag7()


def vraag8():
    print("\nJe vraagt of je vrienden en familie je nog kennen en wat jullie willen doen")
    print("A = Vluchten naar een ander land / B = Wachten tot de oorlog over is")
    while True:
        antw = input()
        if antw == "A":
            print("jullie vluchten naar een ander land, daar zijn jullie voorlopig veilig")
            vraag10()
            break
        elif antw == "B":
            print("Jullie wachten tot de oorlog over is maar dat gebeurd maar niet en jullie worden uit eindelijk gevonden en meegenomen. jullie worden voor levenslang opgesloten")
            break
        else:
            print("ik snap je antwoord niet. Vul een geldig antwoord in: ")
            vraag8()


def vraag9():
    print("\nJe zit veilig maar wilt toch graag weg en je mist je familie, wat doe je")
    print("A = je Vlucht nog verder / B = Je gaat je familie zoeken in je eigen land want je mist ze")
    while True:
        antw = input()
        if antw == "A":
            print("Je vlucht richting het midden van Europa op zoek naar een beter leven")
            vraag11()
            break
        elif antw == "B":
            print("je vind je familie terug maar je zit nu vast in je eigen land")
            vraag12()
            break
        else:
            print("ik snap je antwoord niet. Vul een geldig antwoord in: ")
            vraag9()


def vraag10():
    print("\nEenmaal aangekomen in Europa nemen jullie afscheid van elkaar omdat niet iedereen naar hetzelfde land kan. wat doe jij?")
    print("A = je probeert mee te gaan met 1 bekende / B = je gaat alleen een kant op")
    while True:
        antw = input()
        if antw == "A":
            print("Dat mocht niet en je werd teruggestuurd naar je eigen land en je werd gelijk opgesloten")
            break
        elif antw == "B":
            print("je komt aan in Berlijn en zoekt onderkomen")
            vraag13()
            break
        else:
            print("ik snap je antwoord niet. Vul een geldig antwoord in: ")
            vraag10()


def vraag11():
    print("\nJa mag een land kiezen waar je heen gaat en dan de stad")
    print("A = Duitsland, Berlijn / B = Italië, Rome")
    while True:
        antw = input()
        if antw == "A":
            print("Je gaat richting Berlijn hopend op een veilige toekomst")
            vraag13()
            break
        elif antw == "B":
            print("Je gaat richting Rome alleen onderweg door Italië word je niet fijn aangekeken en doodgestoken omdat een drugscartel dacht dat je hun land in wilde nemen")
            break
        else:
            print("ik snap je antwoord niet. Vul een geldig antwoord in: ")
            vraag11()


def vraag12():
    print("\nJe hebt je familie gevonden maar je wilt weg wat doe je?")
    print("A = Proberen opnieuw te vluchten met je familie / B = Je wordt depressief omdat er geen mogelijkheid is voor vrede of geluk")
    while True:
        antw = input()
        if antw == "A":
            print("je wordt opgepakt en opgesloten")
            break
        elif antw == "B":
            print("je kan de pijn niet meer aan en er valt een bom op jullie huis... niemand overleeft het")
            break
        else:
            print("ik snap je antwoord niet. Vul een geldig antwoord in: ")
            vraag12()


def vraag13():
    print("\nJe bent in Duitsland aangekomen en gaat richting Berlijn maar je wordt tegengehouden door de Douane wat doe je?")
    print("A = Je vertelt dat je een vluchteling bent / B = Je vertelt dat je een asielzoeker bent op zoek naar hulp en een veilige plek")
    while True:
        antw = input()
        if antw == "A":
            print("Je mag in Duitsland verblijven tot de oorlog voorbij is. Gelukkig maar!")
            break
        elif antw == "B":
            print("Je wordt niet geaccepteerd en moet naar een ander land")
            vraag14()
            break
        else:
            print("ik snap je antwoord niet. Vul een geldig antwoord in: ")
            vraag13()


def vraag14():
    print("\n")
    print("A = Nederland / B = Rusland / C = Frankrijk / D = België")
    while True:
        antw = input()
        if antw == "A":
            print("Je gaat naar Nederland")
            vraag15()
            break
        elif antw == "B":
            print("Rusland klinkt leuk je gaat onderweg daar naartoe")
            vraag16()
            break
        elif antw == "C":
            print("Je gaat opweg naar Frankrijk")
            vraag17()
            break
        elif antw == "D":
            print("Ah ja België klinkt leuk!")
            vraag18()
            break
        else:
            print("ik snap je antwoord niet. Vul een geldig antwoord in: ")
            vraag14()


def vraag15():
    print("\nJe komt aan in Nederland bij de gemeente wat doe je?")
    print("A = Je vraagt of je hier mag blijven vanwege oorlog in het Iran / B = Je vraagt voor een veilige werk en woonplek omdat je niet terugkan")
    while True:
        antw = input()
        if antw == "A":
            print("Je mag blijven tot de oorlog voorbij is. Mooi zo!")
            break
        elif antw == "B":
            print("Je mag niet blijven omdat je werk zoekt want dan klopt de economie niet meer je wordt naar een opvangkamp gestuurd in Griekenland")
            vraag19()
            break
        else:
            print("ik snap je antwoord niet. Vul een geldig antwoord in: ")
            vraag15()


def vraag16():
    print("\nJe komt aan in Rusland wat doe je nu?")
    print("A = Je vraagt of je mag blijven / B = Je vraagt voor een werk en slaapplek")
    while True:
        antw = input()
        if antw == "A":
            print("Rusland nam je aanvraag niet zo rustig en heeft je opgesloten. tenminste veilig")
            break
        elif antw == "B":
            print("Rusland vind dit geen reden om te mogen blijven en stuurt je naar een opvangkamp in Griekenland")
            vraag19()
            break
        else:
            print("ik snap je antwoord niet. Vul een geldig antwoord in: ")
            vraag16()


def vraag17():
    print("\nJe komt aan in Frankrijk waar het niet helemaal goed gaat wat doe je nu?")
    print("A = Je wilt blijven en vraag aan of dat mag / B = Je wordt gestuurd naar het opvangamp in Griekenland op aanvraag")
    while True:
        antw = input()
        if antw == "A":
            print("Je mag blijven en je bent veilig voor altijd! nice!")
            break
        elif antw == "B":
            print("Je gaat richting Griekenland omdat het daar veilig is en je wordt daar geaccepteerd. ook omdat Frankrijk geen goede keuze was")
            vraag19()
            break
        else:
            print("ik snap je antwoord niet. Vul een geldig antwoord in: ")
            vraag17()


def vraag18():
    print("\n")
    print("A =  / B = ")
    while True:
        antw = input()
        if antw == "A":
            print("je mag blijven voor een paar maanden maar daarna moet je naar het opvangamp in Griekenland")
            vraag19()
            break
        elif antw == "B":
            print("Je mag niet blijven en wordt teruggestuurd naar je land wat uiteindelijk je dood word")
            break
        else:
            print("ik snap je antwoord niet. Vul een geldig antwoord in: ")
            vraag18()


def vraag19():
    print("\n")
    print("A =  / B = ")
    while True:
        antw = input()
        if antw == "A":
            print("")
            break
        elif antw == "B":
            print("")
            vraag14()
            break
        else:
            print("ik snap je antwoord niet. Vul een geldig antwoord in: ")
            vraag19()


def vraag19():
    print("\nJe komt aan in het opvangamp in Griekenland. Je vindt je familie daar ook en je vrienden jullie bespreken wat jullie doen na de oorlog, wat doen jullie?")
    print("A = Je blijft in Griekenland omdat het daar wel fijn en rustig is / B = Je gaat na de oorlog terug naar je eigen land")
    while True:
        antw = input()
        if antw == "A":
            print("Je mag blijven met je hele familie en alle vrienden! top!")
            break
        elif antw == "B":
            print("Je komt aan in je eigen land na de oorlog het is een puinhoop helaas...")
            vraag20()
            break
        else:
            print("ik snap je antwoord niet. Vul een geldig antwoord in: ")
            vraag19()


def vraag20():
    print("\nAls je terug bent in je huis besluit je alles op te ruimen dat kapot is van je eigen huis dan vraagt iemand of je wilt helpen buiten wat doe je?")
    print("A = Je zegt ja en helpt buiten mee / B = Je zegt nee sorry het is me allemaal even teveel")
    while True:
        antw = input()
        if antw == "A":
            print("Je komt naar buiten en bent dagen aan het werk tot er een ongeluk gebeurd... een gebouw stort in en jij stond eronder je overleeft het niet :( ")
            break
        elif antw == "B":
            print("Je bouwt je eigen huis op en wacht tot er hulp is gekomen van het leger")
            vraag21()
            break
        else:
            print("ik snap je antwoord niet. Vul een geldig antwoord in: ")
            vraag20()


def vraag21():
    print("\nEr is hulp gekomen van het leger alles is verbeterd, het leger vond je een goed persoon die ook mee hielp uiteindelijk en vraagt of je in het leger wilt wat doe je?")
    print("A = Je Accepteerd het aanbod en Helpt mee met alles opbouwen dat kapot is gegaan in elke stad en je vecht nu voor je land! top gozer dat je bent! :) / B = Je zegt dat je je familie echt gemist hebt en dat je liever samen blifjt wonen")
    while True:
        antw = input()
        if antw == "A":
            print("Het leger vindt je geweldig en promoveert je naar een hogere rang. Je leven gaat goed!")
            break
        elif antw == "B":
            print("Het leger snapt je keuze en wenst je veel geluk en succes.")
            break
        else:
            print("ik snap je antwoord niet. Vul een geldig antwoord in: ")
            vraag21()
#=======================================================================================

print("Hallo mijn naam is ", Vluchteling, " waar denk je dat ik vandaan kom?")

vraag1()
