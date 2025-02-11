class Veicolo:
    def __init__(self, marca: str, modello: str, carburante: str):
        if carburante not in ["benzina", "diesel"]:
            raise ValueError("Il carburante deve essere 'benzina' o 'diesel'")

        self.marca = marca
        self.modello = modello
        self.carburante = carburante

    def get_info(self) -> str:
        """Restituisce le informazioni del veicolo."""
        return f"{self.marca} {self.modello} - {self.carburante}"


class Auto(Veicolo):
    def __init__(self, marca: str, modello: str, carburante: str):
        super().__init__(marca, modello, carburante)

    def get_info(self) -> str:
        return f"Auto: {super().get_info()}"


class Camion(Veicolo):
    def __init__(self, marca: str, modello: str, carburante: str):
        super().__init__(marca, modello, carburante)

    def get_info(self) -> str:
        return f"Camion: {super().get_info()}"


class Flotta:
    def __init__(self):
        self.veicoli: list[Veicolo] = []

    def aggiungi_veicolo(self, veicolo: Veicolo) -> None:
        """Aggiunge un veicolo alla flotta."""
        self.veicoli.append(veicolo)

    def visualizza_informazioni(self) -> None:
        """Visualizza le informazioni di tutti i veicoli nella flotta."""
        for veicolo in self.veicoli:
            print(veicolo.get_info())


def main():
    # Creazione della flotta
    flotta = Flotta()

    # Aggiunta di veicoli alla flotta
    auto1 = Auto("Fiat", "Panda", "benzina")
    auto2 = Auto("Volkswagen", "Golf", "diesel")
    camion1 = Camion("Iveco", "Daily", "diesel")

    flotta.aggiungi_veicolo(auto1)
    flotta.aggiungi_veicolo(auto2)
    flotta.aggiungi_veicolo(camion1)

    # Visualizzazione della flotta
    print("\nVeicoli nella flotta aziendale:")
    flotta.visualizza_informazioni()


if __name__ == "__main__":
    main()
