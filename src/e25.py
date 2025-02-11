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

    def cerca_prenotazione(
        self, nome: str | None = None, data: datetime | None = None
    ) -> list[Prenotazione]:
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
