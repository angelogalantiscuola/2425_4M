from datetime import datetime
from typing import List, Optional
from enum import Enum


class TipoClasse(Enum):
    BUSINESS = "Business"
    ECONOMY = "Economy"


class Volo:
    def __init__(
        self,
        numero_volo: str,
        destinazione: str,
        data_ora_partenza: datetime,
        numero_massimo_passeggeri: int,
    ):
        self.numero_volo = numero_volo
        self.destinazione = destinazione
        self.data_ora_partenza = data_ora_partenza
        self.numero_massimo_passeggeri = numero_massimo_passeggeri
        self.prenotazioni: List["Prenotazione"] = []

    def posti_disponibili(self) -> int:
        """Calcola il numero di posti ancora disponibili sul volo."""
        return self.numero_massimo_passeggeri - len(self.prenotazioni)

    def __str__(self) -> str:
        return (
            f"Volo {self.numero_volo} per {self.destinazione} - "
            f"Partenza: {self.data_ora_partenza.strftime('%d/%m/%Y %H:%M')} - "
            f"Posti disponibili: {self.posti_disponibili()}"
        )


class Prenotazione:
    def __init__(self, nome_passeggero: str, tipo_classe: TipoClasse, volo: Volo):
        self.nome_passeggero = nome_passeggero
        self.tipo_classe = tipo_classe
        self.volo = volo

    def __str__(self) -> str:
        return (
            f"Prenotazione per {self.nome_passeggero} - "
            f"Classe: {self.tipo_classe.value} - "
            f"Volo: {self.volo.numero_volo} per {self.volo.destinazione}"
        )


class SistemaPrenotazioni:
    def __init__(self):
        self.voli: List[Volo] = []
        self.prenotazioni: List[Prenotazione] = []

    def aggiungi_volo(self, volo: Volo) -> None:
        """Aggiunge un nuovo volo al sistema."""
        self.voli.append(volo)

    def aggiungi_prenotazione(
        self, nome_passeggero: str, tipo_classe: TipoClasse, numero_volo: str
    ) -> Optional[Prenotazione]:
        """
        Aggiunge una nuova prenotazione se ci sono posti disponibili.
        Restituisce la prenotazione creata o None se non è possibile effettuarla.
        """
        for volo in self.voli:
            if volo.numero_volo == numero_volo and volo.posti_disponibili() > 0:
                prenotazione = Prenotazione(nome_passeggero, tipo_classe, volo)
                self.prenotazioni.append(prenotazione)
                volo.prenotazioni.append(prenotazione)
                return prenotazione
        return None

    def visualizza_voli(self) -> List[Volo]:
        """Restituisce tutti i voli nel sistema."""
        return self.voli

    def visualizza_prenotazioni(self) -> List[Prenotazione]:
        """Restituisce tutte le prenotazioni nel sistema."""
        return self.prenotazioni


def main():
    # Creazione del sistema
    sistema = SistemaPrenotazioni()

    # Aggiunta di voli
    volo1 = Volo(
        "AZ100",
        "Roma-Milano",
        datetime(2024, 2, 15, 10, 30),
        100,
    )
    volo2 = Volo(
        "AZ200",
        "Milano-Napoli",
        datetime(2024, 2, 15, 14, 45),
        80,
    )

    sistema.aggiungi_volo(volo1)
    sistema.aggiungi_volo(volo2)

    # Visualizzazione dei voli disponibili
    print("\nVoli disponibili:")
    for volo in sistema.visualizza_voli():
        print(volo)

    # Effettua alcune prenotazioni
    sistema.aggiungi_prenotazione("Mario Rossi", TipoClasse.BUSINESS, "AZ100")
    sistema.aggiungi_prenotazione("Luigi Verdi", TipoClasse.ECONOMY, "AZ100")
    sistema.aggiungi_prenotazione("Anna Bianchi", TipoClasse.BUSINESS, "AZ200")

    # Visualizzazione delle prenotazioni
    print("\nPrenotazioni effettuate:")
    for prenotazione in sistema.visualizza_prenotazioni():
        print(prenotazione)

    # Verifica dei posti rimanenti
    print("\nStato attuale dei voli:")
    for volo in sistema.visualizza_voli():
        print(volo)


if __name__ == "__main__":
    main()
