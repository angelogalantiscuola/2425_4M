
class MaterialeBiblioteca:
    def __init__(self, titolo, anno_pubblicazione):
        self.titolo = titolo
        self.anno_pubblicazione = anno_pubblicazione
        self.disponibile = True

    def get_titolo(self):
        return self.titolo

    def get_anno_pubblicazione(self):
        return self.anno_pubblicazione

    def is_disponibile(self):
        return self.disponibile

    def prestito(self):
        self.disponibile = False

    def restituzione(self):
        self.disponibile = True

    @staticmethod
    def ricerca(materiali, titolo):
        for materiale in materiali:
            if materiale.get_titolo() == titolo:
                return materiale
        return None


class Libro(MaterialeBiblioteca):
    def __init__(self, titolo, anno_pubblicazione, autore, numero_pagine):
        super().__init__(titolo, anno_pubblicazione)
        self.autore = autore
        self.numero_pagine = numero_pagine

    def get_autore(self):
        return self.autore

    def get_numero_pagine(self):
        return self.numero_pagine


class Rivista(MaterialeBiblioteca):
    def __init__(self, titolo, anno_pubblicazione, numero_edizione, mese_pubblicazione):
        super().__init__(titolo, anno_pubblicazione)
        self.numero_edizione = numero_edizione
        self.mese_pubblicazione = mese_pubblicazione

    def get_numero_edizione(self):
        return self.numero_edizione

    def get_mese_pubblicazione(self):
        return self.mese_pubblicazione


class DVD(MaterialeBiblioteca):
    def __init__(self, titolo, anno_pubblicazione, regista, durata):
        super().__init__(titolo, anno_pubblicazione)
        self.regista = regista
        self.durata = durata

    def get_regista(self):
        return self.regista

    def get_durata(self):
        return self.durata