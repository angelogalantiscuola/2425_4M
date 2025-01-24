## Sistema di Gestione Centro Spaziale

### Traccia

Si richiede di implementare un sistema software per la gestione di un centro spaziale. Il sistema deve gestire il personale, le missioni spaziali e i veicoli spaziali attraverso un insieme di classi interconnesse.

### Specifiche del Sistema

Il sistema è composto da diverse entità principali:

1. **Personale del Centro Spaziale**

   - Ogni membro del personale ha un nome, ruolo, anni di esperienza
   - Tre tipologie specifiche di personale:
     - Astronauti che partecipano alle missioni, hanno le ore di volo
     - Tecnici di controllo che supervisionano i veicoli, hanno una specializzazione
     - Ingegneri di manutenzione che si occupano della manutenzione dei veicoli, hanno delle certificazioni

2. **Missioni Spaziali**

   - Ogni missione ha un codice identificativo, un obiettivo specifico
   - Le missioni possono essere in diversi stati (pianificata, in corso, completata)
   - Ogni missione coinvolge più astronauti e utilizza uno o più veicoli spaziali

3. **Veicoli Spaziali**
   - Ogni veicolo ha un identificativo univoco e un tipo specifico
   - I veicoli hanno uno stato operativo che ne indica la disponibilità: se lo stato è Operativo il veicolo è disponibile, se lo stato è "In Missione" il veicolo non è disponibile
   - Ogni veicolo è assegnato a un tecnico di controllo
   - Più ingegneri possono occuparsi della manutenzione dello stesso veicolo

### Requisiti Funzionali

Il sistema deve permettere di:

1. Gestire le relazioni tra le diverse entità del sistema
2. Assegnare gli astronauti alle missioni
3. Assegnare i veicoli alle missioni
4. Gestire l'assegnazione dei tecnici ai veicoli
5. Produrre statistiche sul personale impiegato nelle missioni
6. Generare report sullo stato delle missioni in corso

### Vincoli:

- Ogni veicolo può essere assegnato a una sola missione alla volta
- Ogni tecnico può gestire più veicoli ma ogni veicolo ha un solo tecnico responsabile
- Gli ingegneri possono lavorare su più veicoli e ogni veicolo può essere mantenuto da più ingegneri
- Gli astronauti possono partecipare a più missioni e ogni missione può avere più astronauti
