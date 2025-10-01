



def show_menu1(): 

#meny som du kan välja vad du vill göra
    print("---- VÄLKOMMEN ----")
    #A,ska inne hålla övervakning av 1. CPU 2.minnesandvänding 3. diskanvänding g
    print("[A] STARTA ÖVERVAKNING")
   #B, ska sak lista den aktiv övervakning, om det inte finns någon aktiv ska det komma upp meddelande om detta
    print("[B] LISTA AKTIV ÖVERVAKNING")
   #C, ska kunna starta ett larm som man kan välja sin gräns i %, detta ska kunna göras i en yttligare meny
    print("[C] SKAPA LARM (kommer en till meny)")
   #D, kunna starta ett övervakningsläge som användaren blir promtad om när det har startas, man ska kunna återgå till huvudmeny
    print("[D] STARTA ÖVERVAKNINGS LÄGE")
   #E, avsluta hela programmet och återgår till terminalen
    print("[E] STÄNG PROGRAM")


#konfigurera larm över: 1.CPU, 2. minne, 3.disk, 4.tillbaka till huvudmenyn. 
def show_menu2():
    print("---SKAPA LARM---")
    print("[A] CPU")
    print("[B] Minne")
    print("[C] Disk")
    print("[D] Tillbaka till huvudmenyn")
#hantera menyvalen, bestämmer vad som ska ske, (ska bytas senare) 
def handle_menu(val):
    val = val.upper()  # Gör det versalkänsligt (A-E)
    if val == "A":
        print("Hello world")
    elif val == "B": 
        print("Hello")
    elif val == "C":
        print("Du har valt C")
    elif val == "D":
        print("Du har valt D")
    elif val == "E":
        print("Programmet avslutas...")
        return False
    # om användaren skulle välja något alvternativ som inte finns, kommer det upp ett meddelande(en liten del av felhantering)
    else: 
        print("Ogiltligt val")
    
    
    return True  

# Kör själva meny-loopen
fortsätt = True
while fortsätt:
    show_menu1()
    användarval = input("Välj ett alternativ (A-E): ")
    fortsätt = handle_menu(användarval)

    go = True
    while go:
        if användarval.upper() == "C":
            show_menu2()
            användarval2 = input("Välj ett alternativ (A-D): ")
            användarval2 = användarval2.upper()
            if användarval2 == "A":
                print("Du har valt CPU")
            elif användarval2 == "B":
                print("Du har valt Minne")
            elif användarval2 == "C":
                print("Du har valt Disk")
            elif användarval2 == "D":
                go = False
            else:
                print("Ogiltligt val")
