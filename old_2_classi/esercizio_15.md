Crea un programma Python che modella un'associazione n-n tra due classi: `Corso` e `Studente`.

- **STUDENTE**: La classe `Studente` dovrebbe avere i seguenti attributi: 
    - `nome`: una stringa che rappresenta il nome della persona. 
    - `cognome`: una stringa che rappresenta il cognome della persona. 
    - `sesso`: "M" se maschio, "F" se femmina 
    - `età`: un intero che rappresenta l'età della persona.

- **CORSO**: La classe `Corso` dovrebbe avere i seguenti attributi: 
    - `id`: una stringa che rappresenta il corso. 
    - `uni_name`: una stringa che rappresenta l'università. 
    - `descrizione`: una descrizione di base del corso. 
    - Una lista di `Studenti`.

La classe `Studente` dovrebbe avere il metodo: 
- `corsi_iscritti()`: un metodo che mostra i corsi in cui lo studente è iscritto.

La classe `Corso` dovrebbe avere i seguenti metodi: 
- `aggiungi_studente`: un metodo che permette di aggiungere uno `Studente` alla lista. 
- `rimuovi_studente`: un metodo che permette di rimuovere uno `Studente` dalla lista 
- `conta_studenti_iscritti`: un metodo che restituisce il numero di studenti iscritti.

Ricorda: Un corso potrebbe avere da 1 a n studenti e uno studente potrebbe essere iscritto a da 1 a n corsi, il che significa:

La classe `Corso` dovrebbe avere una lista di studenti. La classe `Studente` dovrebbe avere una lista di corsi.