
class Dipendente:
    def __init__(self, nome, stipendio):
        self.nome = nome
        self.stipendio = stipendio

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_stipendio(self):
        return self.stipendio

    def set_stipendio(self, stipendio):
        self.stipendio = stipendio


class Manager(Dipendente):
    def __init__(self, nome, stipendio, numero_di_team):
        super().__init__(nome, stipendio)
        self.numero_di_team = numero_di_team

    def get_numero_di_team(self):
        return self.numero_di_team

    def set_numero_di_team(self, numero_di_team):
        self.numero_di_team = numero_di_team


class Sviluppatore(Dipendente):
    def __init__(self, nome, stipendio, linguaggio_di_programmazione):
        super().__init__(nome, stipendio)
        self.linguaggio_di_programmazione = linguaggio_di_programmazione

    def get_linguaggio_di_programmazione(self):
        return self.linguaggio_di_programmazione

    def set_linguaggio_di_programmazione(self, linguaggio_di_programmazione):
        self.linguaggio_di_programmazione = linguaggio_di_programmazione