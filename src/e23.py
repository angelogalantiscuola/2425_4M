from datetime import datetime
from typing import List


class Utente:
    def __init__(self, nome_utente: str, email: str, password: str):
        self.nome_utente = nome_utente
        self.email = email
        self.password = password
        self.immagine_profilo = None
        self.biografia = ""
        self.album = []
        self.foto = []
        self.following = []

    def crea_album(self, titolo: str, descrizione: str) -> "Album":
        nuovo_album = Album(titolo, descrizione, self)
        self.album.append(nuovo_album)
        return nuovo_album

    def carica_foto(
        self, titolo: str, descrizione: str, album: "Album" = None
    ) -> "Foto":
        nuova_foto = Foto(titolo, descrizione, self, album)
        self.foto.append(nuova_foto)
        if album:
            album.aggiungi_foto(nuova_foto)
        return nuova_foto

    def segui_utente(self, utente: "Utente"):
        if utente not in self.following:
            self.following.append(utente)


class Foto:
    def __init__(
        self, titolo: str, descrizione: str, utente: Utente, album: "Album" = None
    ):
        # id() restituisce un identificatore unico per l'oggetto
        self.id = id(self)  # Utilizziamo id() come identificatore unico
        self.titolo = titolo
        self.descrizione = descrizione
        self.data_caricamento = datetime.now()
        self.utente = utente
        self.album = album
        self.commenti = []

    def aggiungi_commento(self, utente: Utente, testo: str) -> "Commento":
        nuovo_commento = Commento(utente, self, testo)
        self.commenti.append(nuovo_commento)
        return nuovo_commento


class Album:
    def __init__(self, titolo: str, descrizione: str, utente: Utente):
        self.titolo = titolo
        self.descrizione = descrizione
        self.utente = utente
        self.foto: List[Foto] = []

    def aggiungi_foto(self, foto: Foto):
        if foto not in self.foto:
            self.foto.append(foto)
            foto.album = self


class Commento:
    def __init__(self, utente: Utente, foto: Foto, testo: str):
        self.utente = utente
        self.foto = foto
        self.testo = testo
        self.data_creazione = datetime.now()


# Esempio di utilizzo
if __name__ == "__main__":
    # Creazione utenti
    mario = Utente("mario_rossi", "mario@email.it", "password123")
    luigi = Utente("luigi_verdi", "luigi@email.it", "password456")

    # Mario crea un album
    album_vacanze = mario.crea_album("Vacanze 2023", "Le mie vacanze estive")

    # Mario carica delle foto
    foto1 = mario.carica_foto("Tramonto", "Un bellissimo tramonto", album_vacanze)
    foto2 = mario.carica_foto("Spiaggia", "Giornata al mare", album_vacanze)

    # Luigi segue Mario
    luigi.segui_utente(mario)

    # Luigi commenta la foto di Mario
    foto1.aggiungi_commento(luigi, "Che bel tramonto!")

    # Stampa lo stato degli oggetti
    print("Utente Mario:", mario.nome_utente)
    print("Utente Luigi:", luigi.nome_utente)
    print("Album di Mario:", album_vacanze.titolo)
    print("Foto 1 di Mario:", foto1.titolo)
    print("Foto 2 di Mario:", foto2.titolo)
    print("Commenti alla foto 1 di Mario:")
    for commento in foto1.commenti:
        print(commento.utente.nome_utente, ":", commento.testo)
    print("Mario segue:", [utente.nome_utente for utente in mario.following])
    print("Luigi segue:", [utente.nome_utente for utente in luigi.following])
