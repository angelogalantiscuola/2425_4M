class Veicolo:
    def __init__(self, targa: str, marca: str, modello: str, carburante: str):
        self._targa = targa
        self._marca = marca
        self._modello = modello
        self._carburante = carburante
    
    def get_info(self) -> str:
        return f"{self._targa} {self._modello} ({self._carburante})"

class Auto(Veicolo):
    # numero posti
    def __init__(self, targa: str, marca: str, modello: str, carburante: str):
        super().__init__(targa, marca, modello, carburante)
        self._posti = 5

    def get_info(self) -> str:
        return f"{super().get_info()} - {self._posti} posti"

class Camion(Veicolo):
    # portata
    def __init__(self, targa: str, marca: str, modello: str, carburante: str, portata: int):
        super().__init__(targa, marca, modello, carburante)
        self._portata = portata
    
    def get_info(self) -> str:
        return f"{super().get_info()} - {self._portata} kg"

class Flotta:
    def __init__(self):
        self._veicoli: list[Veicolo] = []
    
    def aggiungi_veicolo(self, veicolo: Veicolo) -> bool:
        # controlla che il veicolo non sia già presente nella flotta
        for v in self._veicoli:
            if v._targa == veicolo._targa:
                return False
        self._veicoli.append(veicolo)
        return True
    
    def visualizza_flotta(self) -> None:
        for veicolo in self._veicoli:
            print(veicolo.get_info())
    
    def restituisci_flotta(self) -> list[Veicolo]:
        return self._veicoli

class Dipendente:
    def __init__(self, nome: str, cognome: str, cf: str):
        self._nome = nome
        self._cognome = cognome
        self._cf = cf

# Example usage
if __name__ == "__main__":
    flotta = Flotta()
    auto = Auto("AB123CD", "Fiat", "Panda", "benzina")
    camion = Camion("XY456ZW", "Iveco", "Daily", "diesel", 3500)
    dipendente = Dipendente("Mario", "Rossi", "RSSMRA80A01H501A")

    # stampa esito aggiunta veicolo
    if flotta.aggiungi_veicolo(auto):
        print("Auto aggiunta alla flotta")
    else:
        print("Auto già presente nella flotta")

    if flotta.aggiungi_veicolo(auto):
        print("Auto aggiunta alla flotta")
    else:
        print("Auto già presente nella flotta")

    if flotta.aggiungi_veicolo(camion):
        print("Camion aggiunto alla flotta")
    else:
        print("Camion già presente nella flotta")
    
    print("\nLista veicoli:")
    veicoli = flotta.restituisci_flotta()
    for v in veicoli:
        print(v.get_info())