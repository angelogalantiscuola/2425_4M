# Servizio di Streaming

1. Abbiamo un `Utente` che può sottoscrivere un servizio. L'`Utente` ha un `username`, `email`, e può anche creare molteplici `Playlist`.

2. C'è un `Artista` che può creare molti `Album`. L'`Artista` ha un `nome`.

3. Ogni `Album` può contenere molte `Canzoni` e appartiene ad un `Artista`. L'`Album` ha un `titolo`. C'è anche un tipo speciale di `Album`, chiamato `AlbumPremium`, che contiene `contenutoEsclusivo`.

4. Ogni `Canzone` appartiene ad un `Album` e può essere inclusa in molteplici `Playlist`. La `Canzone` ha un `titolo` e `durata`.

5. Una `Playlist` appartiene ad un `Utente` e può contenere molte `Canzoni`. La `Playlist` ha un `nome`.

6. Una `Sottoscrizione` è associata ad un `Utente`. La `Sottoscrizione` ha un `tipo` e `prezzo`.

Ricorda di usare la corretta sintassi PlantUML per definire classi, attributi, relazioni ed ereditarietà.


Ecco un semplice esempio di streaming service.
contiene le sefuenti classi:
"""
- Song
- Album
- PremiumAlbum
- Playlist
- Subscription
- User
- Artist
"""
Contiene anche una funzione che crea gli oggetti e li restituisce.
