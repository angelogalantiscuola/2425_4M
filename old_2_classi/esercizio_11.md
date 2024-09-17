# Creare una classe Bicicletta

Creare una classe `Bicicletta` con i seguenti attributi:
1. `speed` (float)
2. `marcia` (int)

E i seguenti metodi:
1. Un costruttore che inizializzi tutti i parametri a zero.
2. Un metodo `speedUp()` per incrementare la velocità di 1 km/h.
3. Un metodo `speedDown()` per decrementare la velocità di 1 km/h.
4. Un metodo `setMarcia(int nuova_marcia)` per cambiare marcia.
5. Un metodo `__str__()` che stampi il valore di tutti i parametri in sequenza.

Creare la classe `MountainBike` che estende `Bicicletta` aggiungendo i seguenti attributi:
1. `ammortizzatori` (boolean)

E i seguenti metodi:
1. Un costruttore che inizializzi tutti i parametri di `Bicicletta` a zero (si può utilizzare `super()`) e imposti `ammortizzatori` a False.
2. Un metodo `getAmmortizzatori()` per ottenere il valore di `ammortizzatori`.
3. Ridefinire il metodo `__str__()` per la stampa dei valori degli attributi della `Bicicletta` aggiungendo il valore di `ammortizzatori`.

Creare la classe `FatBike` che estende `Bicicletta` aggiungendo i seguenti attributi:
1. `spessore_pneumatico` (int)

E i seguenti metodi:
1. Un costruttore che inizializzi tutti i parametri di `Bicicletta` a zero (si può utilizzare `super()`) e imposti `spessore_pneumatico` al valore desiderato.
2. Un metodo `getSpessorePneumatico()` per ottenere il valore dello spessore dello pneumatico.
3. Ridefinire il metodo `__str__()` per la stampa dei valori degli attributi di `Bicicletta` aggiungendo il valore di `spessore_pneumatico`.