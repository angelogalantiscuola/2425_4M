
class Casa:
    def __init__(self, indirizzo, proprietario):
        self.indirizzo = indirizzo
        self.proprietario = proprietario
        self.stanze = []

    def aggiungi_stanza(self, stanza):
        self.stanze.append(stanza)

    def stampa_stanze(self):
        for stanza in self.stanze:
            print(f"{stanza.nome} ({stanza.superficie} mq)")


class Stanza:
    def __init__(self, nome, superficie):
        self.nome = nome
        self.superficie = superficie