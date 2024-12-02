class Veicolo:
    numero_veicoli = 0

    def __init__(self, tipo, marca):
        self.tipo = tipo
        self.marca = marca
        Veicolo.numero_veicoli += 1

    @classmethod
    def get_numero_veicoli(cls):
        return cls.numero_veicoli