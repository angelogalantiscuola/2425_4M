from datetime import date
from enum import Enum
from typing import Dict, List, Tuple


class CategoriaSpesa(Enum):
    CIBO = "CIBO"
    TRASPORTI = "TRASPORTI"
    CASA = "CASA"
    SVAGO = "SVAGO"
    SALUTE = "SALUTE"
    ALTRO = "ALTRO"


class TipoTransazione(Enum):
    ENTRATA = "ENTRATA"
    USCITA = "USCITA"


class Transazione:
    id_transazione: str
    data: date
    importo: float
    descrizione: str
    tipo: TipoTransazione
    categoria: CategoriaSpesa

    def __init__(
        self,
        id_transazione: str,
        data: date,
        importo: float,
        descrizione: str,
        tipo: TipoTransazione,
        categoria: CategoriaSpesa,
    ) -> None:
        self.id_transazione = id_transazione
        self.data = data
        self.importo = importo
        self.descrizione = descrizione
        self.tipo = tipo
        self.categoria = categoria


class ContoBancario:
    id_conto: str
    nome_conto: str
    saldo_attuale: float
    transazioni: List[Transazione]

    def __init__(self, id_conto: str, nome_conto: str, saldo_iniziale: float = 0) -> None:
        self.id_conto = id_conto
        self.nome_conto = nome_conto
        self.saldo_attuale = saldo_iniziale
        self.transazioni = []

    def saldo_disponibile(self) -> float:
        return self.saldo_attuale

    def media_spese_totali(self) -> float:
        if not self.transazioni:
            return 0.0
        spese = [t.importo for t in self.transazioni if t.tipo == TipoTransazione.USCITA]
        return sum(spese) / len(spese) if spese else 0.0

    def report_mensile(self) -> List[Transazione]:
        oggi: date = date.today()
        return [t for t in self.transazioni if t.data.month == oggi.month and t.data.year == oggi.year]

    def aggiungi_transazione(self, transazione: Transazione) -> None:
        self.transazioni.append(transazione)
        if transazione.tipo == TipoTransazione.ENTRATA:
            self.saldo_attuale += transazione.importo
        else:
            self.saldo_attuale -= transazione.importo


class Utente:
    id_utente: str
    nome_utente: str
    email: str
    conti: List[ContoBancario]

    def __init__(self, id_utente: str, nome_utente: str, email: str) -> None:
        self.id_utente = id_utente
        self.nome_utente = nome_utente
        self.email = email
        self.conti = []

    def registra_transazione(
        self,
        conto: ContoBancario,
        importo: float,
        categoria: CategoriaSpesa,
        descrizione: str,
    ) -> Transazione:
        if conto not in self.conti:
            raise ValueError("Il conto non appartiene all'utente")

        id_transazione: str = f"TX_{len(conto.transazioni) + 1}"
        tipo: TipoTransazione = TipoTransazione.ENTRATA if importo > 0 else TipoTransazione.USCITA
        transazione: Transazione = Transazione(
            id_transazione=id_transazione,
            data=date.today(),
            importo=abs(importo),
            descrizione=descrizione,
            tipo=tipo,
            categoria=categoria,
        )
        conto.aggiungi_transazione(transazione=transazione)
        return transazione

    def totale_spese_mensili(self) -> float:
        oggi: date = date.today()
        totale: float = 0.0
        for conto in self.conti:
            for trans in conto.transazioni:
                if (
                    trans.data.month == oggi.month
                    and trans.data.year == oggi.year
                    and trans.tipo == TipoTransazione.USCITA
                ):
                    totale += trans.importo
        return totale

    def spese_per_categoria(self) -> Dict[CategoriaSpesa, float]:
        spese: Dict[CategoriaSpesa, float] = {categoria: 0.0 for categoria in CategoriaSpesa}
        for conto in self.conti:
            for transazione in conto.transazioni:
                if transazione.tipo == TipoTransazione.USCITA:
                    spese[transazione.categoria] += transazione.importo
        return spese

    def categoria_piu_costosa(self) -> CategoriaSpesa:
        spese: Dict[CategoriaSpesa, float] = self.spese_per_categoria()
        max_categoria: Tuple[CategoriaSpesa, float] = max(spese.items(), key=lambda x: x[1])
        return max_categoria[0]


def main() -> None:
    # Creazione di un utente
    utente: Utente = Utente(id_utente="U1", nome_utente="Mario Rossi", email="mario.rossi@email.com")

    # Creazione di due conti bancari
    conto_principale: ContoBancario = ContoBancario(id_conto="C1", nome_conto="Conto Principale", saldo_iniziale=1000.0)
    conto_risparmi: ContoBancario = ContoBancario(id_conto="C2", nome_conto="Conto Risparmi", saldo_iniziale=5000.0)

    # Aggiunta dei conti all'utente
    utente.conti.extend([conto_principale, conto_risparmi])

    # Registrazione di alcune transazioni
    utente.registra_transazione(
        conto=conto_principale, importo=-50.0, categoria=CategoriaSpesa.CIBO, descrizione="Spesa settimanale"
    )

    utente.registra_transazione(
        conto=conto_principale, importo=-30.0, categoria=CategoriaSpesa.TRASPORTI, descrizione="Benzina"
    )

    utente.registra_transazione(
        conto=conto_principale, importo=1000.0, categoria=CategoriaSpesa.ALTRO, descrizione="Stipendio"
    )

    utente.registra_transazione(
        conto=conto_risparmi, importo=-200.0, categoria=CategoriaSpesa.SVAGO, descrizione="Weekend fuori città"
    )

    # Visualizzazione dei risultati
    print(f"\nUtente: {utente.nome_utente}")
    print(f"Email: {utente.email}")

    for conto in utente.conti:
        print(f"\nConto: {conto.nome_conto}")
        print(f"Saldo disponibile: €{conto.saldo_disponibile():.2f}")
        print(f"Media spese totali: €{conto.media_spese_totali():.2f}")

    print("\nStatistiche spese:")
    spese: Dict[CategoriaSpesa, float] = utente.spese_per_categoria()
    for categoria, importo in spese.items():
        if importo > 0:
            print(f"{categoria.value}: €{importo:.2f}")

    categoria_max: CategoriaSpesa = utente.categoria_piu_costosa()
    print(f"\nCategoria più costosa: {categoria_max.value}")
    print(f"Totale spese mensili: €{utente.totale_spese_mensili():.2f}")


if __name__ == "__main__":
    main()
