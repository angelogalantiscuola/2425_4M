# Associazione 1-n
Creare un programma Python che modella un'associazione 1-n tra due classi, `Aula` e `Studente`.

-STUDENTE
La classe `Studente` dovrebbe avere i seguenti attributi:
- `nome`: una stringa che rappresenta il nome dello studente.
- `cognome`: una stringa che rappresenta il cognome dello studente.
- `sesso`: "M" se maschio, "F" se femmina.
- `eta`: un intero che rappresenta l'età dello studente.

-AULA
La classe `Aula` dovrebbe avere i seguenti attributi:
- `id`: una stringa che rappresenta l'identificativo dell'aula.
- `nome_scuola`: una stringa che rappresenta il nome della scuola.
- `descrizione`: una descrizione di base dell'aula.
- Una lista di `Studenti`.

La classe `Aula` dovrebbe avere i seguenti metodi:
- `aggiungi_studente`: un metodo che permette di aggiungere uno `Studente` alla lista.
- `rimuovi_studente`: un metodo che permette di rimuovere uno `Studente` dalla lista.
- `conta_studenti_iscritti`: un metodo che restituisce il numero di studenti iscritti.
