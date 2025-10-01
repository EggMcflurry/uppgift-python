# uppgift-python

Anteckningar till slutuppgift/Dev-log

upplägg av program: 
bygga en meny, det måste ha 5 olika val som man kan göra
starta en övervakning:CPU användning, minnesanvändning, diskanvändning
Lista aktiv övervakning: 
Skapa larm:((1)måste vara en till meny) konfigurera larm över: 1.CPU, 2. minne, 3.disk, 4.tillbaka till huvudmenyn. 
användaren ska kunna välja en nivå, när det gjorts visas huvudmenyn igen.
larm för CPU användning satt till 80%
måste matas in som en siffra mellan 1-100% och matas nonsens in ska användaren få ett felmeddelande.

Starta övervakningsläge: användaren ska få ett meddelande om att övervakningen har startas, en sträng ska loopas med jämna mellanrum (ex: 1-2 min) som meddelar att övervakningen är aktiv, man ska också ha möjlighet att gå tillbaka till huvudmenyn (exempel på hur det ska se ut finns i uppgiften) 

För att få koden snyggare och att se mer städad, kommer jag att bygga funktioner i andra filer som sedan importeras in i main(): filen.
Main-filen kommer vara huvud-filen för detta projekt, jag vill att det ska vara så rent och lättläst som möjligt. 
