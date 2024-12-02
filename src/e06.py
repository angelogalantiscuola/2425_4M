
class Pagamento:
    def processa_pagamento(self):
        raise NotImplementedError("Questo metodo deve essere sovrascritto dalle classi derivate")

class CartaDiCredito(Pagamento):
    def __init__(self, nome, numero, scadenza, cvv):
        self.nome = nome
        self.numero = numero
        self.scadenza = scadenza
        self.cvv = cvv

    def processa_pagamento(self):
        print(f"Elaborazione pagamento con Carta di Credito per {self.nome}")

class PayPal(Pagamento):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def processa_pagamento(self):
        print(f"Elaborazione pagamento con PayPal per {self.email}")

def effettua_pagamento(metodo_di_pagamento: Pagamento):
    metodo_di_pagamento.processa_pagamento()