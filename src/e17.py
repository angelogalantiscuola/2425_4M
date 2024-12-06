
class Insegnante:
    def __init__(self, nome, cognome, strumento):
        self.nome = nome
        self.cognome = cognome
        self.strumento = strumento
        self.studenti = []

    def aggiungi_studente(self, studente):
        if studente not in self.studenti:
            self.studenti.append(studente)


class Studente:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        self.corsi = []
        self.insegnante = None

    def set_insegnante(self, insegnante):
        self.insegnante = insegnante
        insegnante.aggiungi_studente(self)

    def iscrivi_corso(self, corso):
        if corso not in self.corsi:
            self.corsi.append(corso)
            # corso.aggiungi_studente(self)
            corso.studenti.append(self)


class Corso:
    def __init__(self, nome, durata):
        self.nome = nome
        self.durata = durata
        self.studenti = []

    def aggiungi_studente(self, studente):
        if studente not in self.studenti:
            self.studenti.append(studente)

def main():
    # Creazione degli insegnanti
    insegnante1 = Insegnante("Mario", "Rossi", "Pianoforte")
    insegnante2 = Insegnante("Luca", "Bianchi", "Chitarra")

    # Creazione degli studenti
    studente1 = Studente("Anna", "Verdi")
    studente2 = Studente("Marco", "Neri")

    # Assegnazione degli insegnanti agli studenti
    studente1.set_insegnante(insegnante1)
    studente2.set_insegnante(insegnante2)

    # Creazione dei corsi
    corso1 = Corso("Teoria Musicale", "3 mesi")
    corso2 = Corso("Tecnica Pianistica", "6 mesi")

    # Iscrizione degli studenti ai corsi
    studente1.iscrivi_corso(corso1)
    studente1.iscrivi_corso(corso2)
    studente2.iscrivi_corso(corso1)

    # Stampa delle informazioni
    print(f"{studente1.nome} {studente1.cognome} segue i seguenti corsi:")
    for corso in studente1.corsi:
        print(f"- {corso.nome} ({corso.durata})")
    print(f"Ha come insegnante {studente1.insegnante.nome} {studente1.insegnante.cognome}")
    print()

    print(f"{studente2.nome} {studente2.cognome} segue i seguenti corsi:")
    for corso in studente2.corsi:
        print(f"- {corso.nome} ({corso.durata})")
    print(f"Ha come insegnante {studente2.insegnante.nome} {studente2.insegnante.cognome}")
    print()


if __name__ == "__main__":
    main()
