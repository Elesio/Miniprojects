ifNummer = 57 #mit 57 als Zahl wird nicht die ganze Zeit die Konsole vollgespammt
erklärung="Es gibt wohl nix um einfach eine standard Variable zu kreieren..."
erklärung='Jetzt sind hier zwar die char Dinger drum herum aber es kommt trotzdem ein String raus weil Python beide für Strings akzeptiert'

nummerAlsString = str(5)
nummerAlsInt = int(5)
nummerAlsFloat = float(5)

#print(type(nummerAlsString))
#print(type(nummerAlsInt))
#print(type(nummerAlsFloat))

'''
jaja notice me senpai ich bin auch ein Kommentar aber halt multilined
'''

wort1 = wort2 = wort3 = "wir jetzt sind alle gleich hab ich jetzt Rassismus gelöst?" #Die muss ich nichtmal initialisieren das ist schon irgendwie cool
#print(wort1,wort2,wort3)
wort1, wort2, wort3 = "Jetzt sind", "wir leider", "nicht mehr gleich"
#print(wort1,wort2,wort3)

#print(1+1+2+2)        <-- + beim printen von Zahlen
#print("1+1 "+"2+2")   <-- + beim printen von Strings
#print(1+1, 2+2)       <-- , zum tatsächlich seperieren
 

quasiEinArray = [1,1,2,3,5,8,13,21,34]
fibonacci1, fibonacci2, fibonacci3, fibonacci14, fibonacci5, fibonacci6, fibonacci7, fibonacci8, fibonacci9 = quasiEinArray
#print(quasiEinArray)
#print(fibonacci5)

if ifNummer != 57:
    if ifNummer > 100:
        print("Irgendwas über 100")
    elif ifNummer == 100:
        print("Genau 100")
    else:
        print("irgendwas unter 100")

num1 = 5
def add():
    global num2 #direkt den Werte festlegen geh wohl nicht
    num2 = 8    #tja dann halt hier
    print(num1 + num2)
#add()
#print("num2(",num2, ") kann jetzt auch ausßerhalb der Methoden genutzt werden")

gelb = {
    "hell" : "ecec53",
    "normal" : "ffff00",
    "dunkel" : "b8b814"
} #ein actually sinnvolles Dictionary
#print(gelb["hell"])