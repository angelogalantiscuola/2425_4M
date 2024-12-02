
class Piatto:
    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo
        self.disponibile = True

    def get_nome(self):
        return self.nome

    def get_prezzo(self):
        return self.prezzo

    def is_disponibile(self):
        return self.disponibile

    def ordina(self):
        self.disponibile = False

    def disponi(self):
        self.disponibile = True

    def __str__(self):
        return f"{self.nome} - {self.prezzo}€ - {'Disponibile' if self.disponibile else 'Non disponibile'}"


class Antipasto(Piatto):
    def __init__(self, nome, prezzo, ingredienti, porzione):
        super().__init__(nome, prezzo)
        self.ingredienti = ingredienti
        self.porzione = porzione

    def get_ingredienti(self):
        return self.ingredienti

    def get_porzione(self):
        return self.porzione

    def __str__(self):
        return f"{super().__str__()} - Ingredienti: {', '.join(self.ingredienti)} - Porzione: {self.porzione}"


class Primo(Piatto):
    def __init__(self, nome, prezzo, tipo_pasta, sugo):
        super().__init__(nome, prezzo)
        self.tipo_pasta = tipo_pasta
        self.sugo = sugo

    def get_tipo_pasta(self):
        return self.tipo_pasta

    def get_sugo(self):
        return self.sugo

    def __str__(self):
        return f"{super().__str__()} - Tipo Pasta: {self.tipo_pasta} - Sugo: {self.sugo}"


class Secondo(Piatto):
    def __init__(self, nome, prezzo, tipo_carne, cottura):
        super().__init__(nome, prezzo)
        self.tipo_carne = tipo_carne
        self.cottura = cottura

    def get_tipo_carne(self):
        return self.tipo_carne

    def get_cottura(self):
        return self.cottura

    def __str__(self):
        return f"{super().__str__()} - Tipo Carne: {self.tipo_carne} - Cottura: {self.cottura}"


class Dolce(Piatto):
    def __init__(self, nome, prezzo, tipo_dolce, calorie):
        super().__init__(nome, prezzo)
        self.tipo_dolce = tipo_dolce
        self.calorie = calorie

    def get_tipo_dolce(self):
        return self.tipo_dolce

    def get_calorie(self):
        return self.calorie

    def __str__(self):
        return f"{super().__str__()} - Tipo Dolce: {self.tipo_dolce} - Calorie: {self.calorie}"


def calcola_conto(piatti):
    return sum(piatto.get_prezzo() for piatto in piatti)


def stampa_menu(piatti):
    for piatto in piatti:
        print(piatto)