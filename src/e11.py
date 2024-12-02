
class Ricetta:
    def __init__(self, nome, tempo_preparazione, ingredienti, difficolta):
        self.nome = nome
        self.tempo_preparazione = tempo_preparazione
        self.ingredienti = ingredienti
        self.difficolta = difficolta

    def __str__(self):
        return f"{self.nome} - {self.tempo_preparazione} min - Difficoltà: {self.difficolta}"

    def aggiungi_ingrediente(self, ingrediente):
        self.ingredienti.append(ingrediente)


class Primo(Ricetta):
    def __init__(self, nome, tempo_preparazione, ingredienti, difficolta, tipo_pasta, sugo):
        super().__init__(nome, tempo_preparazione, ingredienti, difficolta)
        self.tipo_pasta = tipo_pasta
        self.sugo = sugo


class Secondo(Ricetta):
    def __init__(self, nome, tempo_preparazione, ingredienti, difficolta, tipo_carne, cottura):
        super().__init__(nome, tempo_preparazione, ingredienti, difficolta)
        self.tipo_carne = tipo_carne
        self.cottura = cottura


class Dolce(Ricetta):
    def __init__(self, nome, tempo_preparazione, ingredienti, difficolta, zucchero, tipo_dolce):
        super().__init__(nome, tempo_preparazione, ingredienti, difficolta)
        self.zucchero = zucchero
        self.tipo_dolce = tipo_dolce


def verifica_ingredienti(ricette, disponibili):
    return [ricetta for ricetta in ricette if all(ingrediente in disponibili for ingrediente in ricetta.ingredienti)]


def stampa_ricette(ricette):
    for ricetta in ricette:
        print(ricetta)