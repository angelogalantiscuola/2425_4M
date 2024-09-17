Progetta un diagramma di classe UML e un programma Python per una piattaforma di social media. Concentrati sulla rappresentazione degli utenti, dei post e delle loro relazioni. Utilizza l'ereditarietà per modellare diversi tipi di post e utenti.

1. **Utente:**
   - Attributi: UserID, Username, Email, Password, ListaAmici, ecc.
   - Metodi: AggiungiAmico, RimuoviAmico, PubblicaContenuto, ecc.

2. **UtenteRegolare (Derivato da Utente):**
   - Attributi aggiuntivi: Interessi, RegistroAttività, ecc.
   - Metodi: MiPiacePost, CommentaPost, ecc.

3. **UtenteBusiness (Derivato da Utente):**
   - Attributi aggiuntivi: BusinessID, Prodotti/Servizi, RecensioniClienti, ecc.
   - Metodi: Pubblicità, RispondiAlleRecensioni, ecc.

4. **Post:**
   - Attributi: PostID, Contenuto, Timestamp, ConteggioMiPiace, Commenti, ecc.
   - Metodi: MiPiace, Commenta, Condividi, ecc.

5. **PostTesto (Derivato da Post):**
   - Attributi aggiuntivi: ConteggioParole, Lingua, ecc.
   - Metodi: AnalizzaSentimento, ecc.

6. **PostImmagine (Derivato da Post):**
   - Attributi aggiuntivi: URLImmagine, Risoluzione, FiltriApplicati, ecc.
   - Metodi: ApplicaFiltro, TaggaPersone, ecc.

Stabilisci associazioni come:
- Gli utenti hanno una lista di amici e pubblicano contenuti.
- Gli utenti regolari interagiscono con i post attraverso mi piace e commenti.
- Gli utenti business fanno pubblicità e rispondono alle recensioni dei clienti.
- Differenziazione tra PostTesto e PostImmagine.

Considera come l'ereditarietà permette una rappresentazione più organizzata dei tipi di utenti e post. Spiega le tue scelte di progettazione e qualsiasi ipotesi fatta.
