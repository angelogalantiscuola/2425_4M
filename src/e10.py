
class Frazione:
    def __init__(self, numeratore, denominatore):
        self.numeratore = numeratore
        self.denominatore = denominatore

    def __add__(self, other):
        return Frazione(self.numeratore + other.numeratore, self.denominatore)

    def __sub__(self, other):
        return Frazione(self.numeratore - other.numeratore, self.denominatore)

    def __mul__(self, other):
        return Frazione(self.numeratore * other.numeratore, self.denominatore * other.denominatore)

    def __str__(self):
        return f"Frazione({self.numeratore}, {self.denominatore})"