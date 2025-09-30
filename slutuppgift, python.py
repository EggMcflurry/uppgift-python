def show_menu(): 

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
    show_menu()
    användarval = input("Välj ett alternativ (A-E): ")
    fortsätt = handle_menu(användarval)
