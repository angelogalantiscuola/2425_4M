
class Calcolatrice:
    @staticmethod
    def addizione(a, b):
        return a + b

    @staticmethod
    def sottrazione(a, b):
        return a - b

    @staticmethod
    def moltiplicazione(a, b):
        return a * b

    @staticmethod
    def divisione(a, b):
        if b == 0:
            raise ZeroDivisionError("Divisione per zero non permessa")
        return a / b