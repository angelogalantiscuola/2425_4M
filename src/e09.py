
class Libro:
    def __init__(self, titolo, autore, pagine):
        self._titolo = titolo
        self._autore = autore
        self._pagine = pagine

    @property
    def titolo(self):
        return self._titolo

    @titolo.setter
    def titolo(self, value):
        if not value:
            raise ValueError("Il titolo non può essere una stringa vuota.")
        self._titolo = value

    @property
    def autore(self):
        return self._autore

    @autore.setter
    def autore(self, value):
        if not value:
            raise ValueError("L'autore non può essere una stringa vuota.")
        self._autore = value

    @property
    def pagine(self):
        return self._pagine

    @pagine.setter
    def pagine(self, value):
        if value <= 0:
            raise ValueError("Il numero di pagine deve essere un numero positivo.")
        self._pagine = value