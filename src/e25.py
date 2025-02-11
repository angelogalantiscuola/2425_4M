from datetime import datetime
from enum import Enum


class StatoPrenotazione(Enum):
    CONFERMATA = "confermata"
    IN_ATTESA = "in attesa"
    CANCELLATA = "cancellata"


class Prenotazione:
    def __init__(
        self,
        nome_cliente: str,
        data_ora: datetime,
        num_persone: int,
        stato: StatoPrenotazione = StatoPrenotazione.IN_ATTESA,
    ):
        self.nome_cliente = nome_cliente
        self.data_ora = data_ora
        self.num_persone = num_persone
        self.stato = stato

    def __str__(self) -> str:
        return (
            f"Prenotazione per {self.nome_cliente} - "
            f"{self.data_ora.strftime('%d/%m/%Y %H:%M')} - "
            f"{self.num_persone} persone - "
            f"Stato: {self.stato.value}"
        )


class GestionePrenotazioni:
    def __init__(self):
        self.prenotazioni: list[Prenotazione] = []

    def aggiungi_prenotazione(self, prenotazione: Prenotazione) -> None:
        """Aggiunge una nuova prenotazione al sistema."""
        self.prenotazioni.append(prenotazione)

    def cerca_prenotazione(self, nome: str | None = None, data: datetime | None = None) -> list[Prenotazione]:
        """Cerca prenotazioni per nome del cliente o data."""
        risultati = []
        for p in self.prenotazioni:
            if nome and nome.lower() in p.nome_cliente.lower():
                risultati.append(p)
            elif data and p.data_ora.date() == data.date():
                risultati.append(p)
        return risultati

    def visualizza_prenotazioni(self) -> list[Prenotazione]:
        """Restituisce tutte le prenotazioni nel sistema."""
        return self.prenotazioni

    def cancella_prenotazione(self, nome_cliente: str, data_ora: datetime) -> bool:
        """Cancella una prenotazione specifica."""
        for p in self.prenotazioni:
            if (
                p.nome_cliente.lower() == nome_cliente.lower()
                and p.data_ora == data_ora
                and p.stato != StatoPrenotazione.CANCELLATA
            ):
                p.stato = StatoPrenotazione.CANCELLATA
                return True
        return False


def main():
    # Create reservation management system
    sistema = GestionePrenotazioni()

    # Add some example reservations
    prenotazioni = [
        Prenotazione("Mario Rossi", datetime(2024, 2, 14, 20, 30), 4),
        Prenotazione("Luigi Verdi", datetime(2024, 2, 14, 19, 00), 2),
        Prenotazione("Anna Bianchi", datetime(2024, 2, 15, 21, 00), 6),
    ]

    for p in prenotazioni:
        sistema.aggiungi_prenotazione(p)
        print(f"Aggiunta: {p}")

    print("\nTutte le prenotazioni:")
    for p in sistema.visualizza_prenotazioni():
        print(p)

    print("\nRicerca per nome 'mario':")
    risultati = sistema.cerca_prenotazione(nome="mario")
    for p in risultati:
        print(p)

    print("\nRicerca per data 14/02/2024:")
    data_ricerca = datetime(2024, 2, 14)
    risultati = sistema.cerca_prenotazione(data=data_ricerca)
    for p in risultati:
        print(p)

    # Try to cancel a reservation
    if sistema.cancella_prenotazione("Mario Rossi", datetime(2024, 2, 14, 20, 30)):
        print("\nPrenotazione cancellata con successo")

    print("\nStato finale delle prenotazioni:")
    for p in sistema.visualizza_prenotazioni():
        print(p)


if __name__ == "__main__":
    main()
