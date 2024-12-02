
class Auto:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
        self.motore = None

    def associa_motore(self, motore):
        if self.motore is not None:
            self.motore.auto = None
        self.motore = motore
        if motore.auto is not self:
            motore.associa_auto(self)


class Motore:
    def __init__(self, numero_seriale, tipo):
        self.numero_seriale = numero_seriale
        self.tipo = tipo
        self.auto = None

    def associa_auto(self, auto):
        if self.auto is not None:
            self.auto.motore = None
        self.auto = auto
        if auto.motore is not self:
            auto.associa_motore(self)