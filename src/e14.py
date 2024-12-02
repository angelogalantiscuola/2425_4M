
class Studente:
    def __init__(self, nome, matricola):
        self.nome = nome
        self.matricola = matricola
        self.corsi = []

    def aggiungi_corso(self, corso):
        if corso not in self.corsi:
            self.corsi.append(corso)
            corso.aggiungi_studente(self)


class Corso:
    def __init__(self, titolo, codice):
        self.titolo = titolo
        self.codice = codice
        self.studenti = []

    def aggiungi_studente(self, studente):
        if studente not in self.studenti:
            self.studenti.append(studente)
            studente.aggiungi_corso(self)