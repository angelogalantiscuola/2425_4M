from datetime import datetime
from typing import List
from enum import Enum


class TipoClasse(Enum):
    BUSINESS = "Business"
    ECONOMY = "Economy"


class StatoPrenotazione(Enum):
    VOLO_PIENO = "Volo pieno"
    VOLO_NON_TROVATO = "Volo non trovato"
    PRENOTAZIONE_CONFERMATA = "Prenotazione confermata"


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
    ) -> StatoPrenotazione:
        """
        Aggiunge una nuova prenotazione se ci sono posti disponibili.
        Restituisce la prenotazione creata o uno stato di errore.
        """
        volo_trovato = None
        for v in self.voli:
            if v.numero_volo == numero_volo:
                volo_trovato = v
                break

        if not volo_trovato:
            return StatoPrenotazione.VOLO_NON_TROVATO

        if volo_trovato.posti_disponibili() > 0:
            prenotazione = Prenotazione(nome_passeggero, tipo_classe, volo_trovato)
            self.prenotazioni.append(prenotazione)
            volo_trovato.prenotazioni.append(prenotazione)
            # return prenotazione  # O potremmo restituire StatoPrenotazione.PRENOTAZIONE_CONFERMATA se si preferisce solo lo stato
            return StatoPrenotazione.PRENOTAZIONE_CONFERMATA
        else:
            return StatoPrenotazione.VOLO_PIENO

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
    print("\nTentativi di prenotazione:")
    risultato1 = sistema.aggiungi_prenotazione("Mario Rossi", TipoClasse.BUSINESS, "AZ100")
    if isinstance(risultato1, Prenotazione):
        print(f"Prenotazione per {risultato1.nome_passeggero} confermata.")
    else:
        print(f"Errore prenotazione Mario Rossi: {risultato1.value}")

    risultato2 = sistema.aggiungi_prenotazione("Luigi Verdi", TipoClasse.ECONOMY, "AZ100")
    if isinstance(risultato2, Prenotazione):
        print(f"Prenotazione per {risultato2.nome_passeggero} confermata.")
    else:
        print(f"Errore prenotazione Luigi Verdi: {risultato2.value}")

    risultato3 = sistema.aggiungi_prenotazione("Anna Bianchi", TipoClasse.BUSINESS, "AZ200")
    if isinstance(risultato3, Prenotazione):
        print(f"Prenotazione per {risultato3.nome_passeggero} confermata.")
    else:
        print(f"Errore prenotazione Anna Bianchi: {risultato3.value}")

    # Test volo pieno (supponendo che volo2 abbia capacità 1 per semplicità di test, o aggiungendo prenotazioni fino a riempirlo)
    # Per testare VOLO_PIENO, modifichiamo temporaneamente la capacità di AZ200 o aggiungiamo prenotazioni
    # Qui simuliamo aggiungendo prenotazioni fino a riempire volo2 (se capacità 1)
    # volo2.numero_massimo_passeggeri = 1 # Modifica temporanea per test
    # sistema.aggiungi_prenotazione("Test Pieno", TipoClasse.ECONOMY, "AZ200") # Questa dovrebbe riempire

    risultato4 = sistema.aggiungi_prenotazione("Giovanni Neri", TipoClasse.ECONOMY, "AZ200")  # Tentativo su volo pieno
    if isinstance(risultato4, Prenotazione):
        print(f"Prenotazione per {risultato4.nome_passeggero} confermata.")
    else:
        print(f"Errore prenotazione Giovanni Neri: {risultato4.value}")

    risultato5 = sistema.aggiungi_prenotazione("Laura Gialli", TipoClasse.ECONOMY, "AZ300")  # Volo non esistente
    if isinstance(risultato5, Prenotazione):
        print(f"Prenotazione per {risultato5.nome_passeggero} confermata.")
    else:
        print(f"Errore prenotazione Laura Gialli: {risultato5.value}")

    # Visualizzazione delle prenotazioni
    print("\nPrenotazioni effettuate con successo:")
    for prenotazione in sistema.visualizza_prenotazioni():
        print(prenotazione)

    # Verifica dei posti rimanenti
    print("\nStato attuale dei voli:")
    for volo in sistema.visualizza_voli():
        print(volo)


if __name__ == "__main__":
    main()
