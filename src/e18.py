class Allenatore:
    def __init__(self, nome, cognome, specializzazione):
        self.nome = nome
        self.cognome = cognome
        self.specializzazione = specializzazione
        self.membri = []
        self.corsi = []


class Membro:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        self.allenatore = None
        self.corsi = []
        self.scheda_allenamento = None

    def set_allenatore(self, allenatore):
        self.allenatore = allenatore
        allenatore.membri.append(self)

    def iscrivi_corso(self, corso):
        self.corsi.append(corso)
        corso.iscritti.append(self)

    def set_scheda_allenamento(self, scheda):
        self.scheda_allenamento = scheda


class Corso:
    def __init__(self, nome, durata, allenatore):
        self.nome = nome
        self.durata = durata
        self.allenatore = allenatore
        self.iscritti = []
        allenatore.corsi.append(self)


class SchedaAllenamento:
    def __init__(self, membro, esercizi):
        self.membro = membro
        self.esercizi = esercizi
        membro.scheda_allenamento = self
