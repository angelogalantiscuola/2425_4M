# Associazione 1-1
Creare un programma Python che modella un'associazione 1-1 tra due classi, `Persona` e `Passaporto`.

La classe `Persona` dovrebbe avere i seguenti attributi:

- `nome`: una stringa che rappresenta il nome della persona.
- `eta`: un intero che rappresenta l'età della persona.
- `passaporto`: un'istanza della classe `Passaporto` che rappresenta il passaporto della persona. Inizialmente dovrebbe essere None.

La classe `Persona` dovrebbe avere anche un metodo `emetti_passaporto` che prende come parametri un numero di passaporto e un paese di emissione, crea un nuovo oggetto `Passaporto` e lo assegna all'attributo `passaporto`.

La classe `Passaporto` dovrebbe avere i seguenti attributi:

- `numero_passaporto`: una stringa che rappresenta il numero del passaporto.
- `paese_di_emissione`: una stringa che rappresenta il paese di emissione.

(Opzionale:
- `persona`: un'istanza della classe `Persona` che rappresenta il titolare del passaporto. Inizialmente dovrebbe essere None.
La classe `Passaporto` dovrebbe avere anche un metodo `imposta_persona` che prende un oggetto `Persona` come parametro e lo assegna all'attributo `persona`.)

Dimostra l'associazione 1-1 creando un oggetto `Persona` e utilizzando il metodo `emetti_passaporto` per creare un oggetto `Passaporto`.

Nota: In un'associazione 1-1, un'istanza di una classe (ad es. `Persona`) è associata esattamente a un'istanza di un'altra classe (ad es. `Passaporto`), e viceversa.