class Film:
    def __init__(self, titolo: str, regista: str, anno: int, genere: str, valutazione: int):
        if not 1 <= valutazione <= 10:
            raise ValueError("La valutazione deve essere compresa tra 1 e 10")

        self.titolo = titolo
        self.regista = regista
        self.anno = anno
        self.genere = genere
        self.valutazione = valutazione

    def __str__(self) -> str:
        return f"{self.titolo} ({self.anno}) - Diretto da {self.regista} - {self.genere} - Voto: {self.valutazione}/10"


class Libreria:
    def __init__(self):
        self.films: list[Film] = []

    def aggiungi_film(self, film: Film) -> None:
        """Aggiunge un nuovo film alla libreria."""
        self.films.append(film)

    def cerca_film(self, chiave: str) -> list[Film]:
        """Cerca film per titolo o regista."""
        risultati = []
        chiave = chiave.lower()
        for film in self.films:
            if chiave in film.titolo.lower() or chiave in film.regista.lower():
                risultati.append(film)
        return risultati

    def visualizza_film(self) -> list[Film]:
        """Restituisce tutti i film presenti nella libreria."""
        return self.films

    def media_valutazioni(self) -> float | None:
        """Calcola la valutazione media dei film nella libreria."""
        if not self.films:
            return None
        return sum(film.valutazione for film in self.films) / len(self.films)


def main():
    # Creazione della libreria
    libreria = Libreria()

    # Aggiunta di alcuni film
    film1 = Film("Il Padrino", "Francis Ford Coppola", 1972, "drammatico", 10)
    film2 = Film("Pulp Fiction", "Quentin Tarantino", 1994, "azione", 9)
    film3 = Film("La vita è bella", "Roberto Benigni", 1997, "drammatico", 8)

    libreria.aggiungi_film(film1)
    libreria.aggiungi_film(film2)
    libreria.aggiungi_film(film3)

    # Visualizzazione di tutti i film
    print("\nTutti i film nella libreria:")
    for film in libreria.visualizza_film():
        print(film)

    # Ricerca di film
    print("\nRicerca film per 'Tarantino':")
    for film in libreria.cerca_film("Tarantino"):
        print(film)

    # Calcolo della media delle valutazioni
    media = libreria.media_valutazioni()
    if media:
        print(f"\nMedia delle valutazioni: {media:.1f}/10")


if __name__ == "__main__":
    main()
