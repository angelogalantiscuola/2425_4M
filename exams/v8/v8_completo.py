from enum import Enum
from datetime import date, datetime
from typing import List, Dict, Optional
import uuid


class TipoMiele(Enum):
    ACACIA = "Acacia"
    TIGLIO = "Tiglio"
    CASTAGNO = "Castagno"
    MILLEFIORI = "Millefiori"
    EUCALIPTO = "Eucalipto"
    ALTRO = "Altro"


class Sciame:
    def __init__(self, id_sciame: str, numero_api_stimato: int, ha_regina: bool):
        self.id_sciame: str = id_sciame
        self.numero_api_stimato: int = numero_api_stimato
        self.ha_regina: bool = ha_regina


class RaccoltaMiele:
    def __init__(self, data_raccolta: date, quantita_kg: float, tipo: TipoMiele, note: Optional[str] = None):
        self.id_raccolta: str = str(uuid.uuid4())  # Auto-generate id for simplicity
        self.data_raccolta: date = data_raccolta
        self.quantita_kg: float = quantita_kg
        self.tipo: TipoMiele = tipo
        self.note: Optional[str] = note


class Alveare:
    def __init__(self, id_alveare: str, posizione_gps: str, data_installazione: date, sciame: Sciame):
        self.id_alveare: str = id_alveare
        self.posizione_gps: str = posizione_gps
        self.data_installazione: date = data_installazione
        self.sciame: Sciame = sciame
        self.raccolte: List[RaccoltaMiele] = []

    def aggiungi_raccolta(self, raccolta: RaccoltaMiele) -> None:
        self.raccolte.append(raccolta)

    def produzione_totale(self) -> float:
        return sum(raccolta.quantita_kg for raccolta in self.raccolte)

    def media_raccolte(self) -> float:
        if not self.raccolte:
            return 0.0
        return self.produzione_totale() / len(self.raccolte)

    def eta_giorni(self) -> int:
        return (date.today() - self.data_installazione).days


class Apicoltore:
    def __init__(self, id_apicoltore: str, nome: str, numero_licenza: str):
        self.id_apicoltore: str = id_apicoltore
        self.nome: str = nome
        self.numero_licenza: str = numero_licenza
        self.alveari: List[Alveare] = []

    def aggiungi_alveare(self, alveare: Alveare) -> None:
        self.alveari.append(alveare)

    def registra_raccolta(
        self,
        alveare: Alveare,
        quantita_kg: float,
        tipo: TipoMiele,
        data_raccolta: Optional[date] = None,
        note: Optional[str] = None,
    ) -> RaccoltaMiele:
        if data_raccolta is None:
            data_raccolta = date.today()

        raccolta = RaccoltaMiele(data_raccolta=data_raccolta, quantita_kg=quantita_kg, tipo=tipo, note=note)

        # Find the alveare in the apicoltore's list and add the raccolta
        # This assumes the passed 'alveare' object is one of the apicoltore's alveari.
        # For a more robust system, we might search by id.
        found_alveare = next((a for a in self.alveari if a.id_alveare == alveare.id_alveare), None)
        if found_alveare:
            found_alveare.aggiungi_raccolta(raccolta)
        else:
            # Or handle error: print("Errore: Alveare non trovato per questo apicoltore.")
            # For now, let's assume the alveare object passed is correct and already managed.
            # If the alveare object itself is passed (and it's one of the apicoltore's),
            # we can just call its method.
            alveare.aggiungi_raccolta(raccolta)
            # If the alveare was not in self.alveari, this might be an issue depending on desired logic.
            # The current v8.py example implies the alveare objects are directly manipulated.

        return raccolta

    def produzione_per_tipo(self) -> Dict[TipoMiele, float]:
        produzione: Dict[TipoMiele, float] = {tipo: 0.0 for tipo in TipoMiele}
        for alveare in self.alveari:
            for raccolta in alveare.raccolte:
                produzione[raccolta.tipo] += raccolta.quantita_kg
        return produzione

    def alveare_piu_produttivo(self) -> Optional[Alveare]:
        if not self.alveari:
            return None
        return max(self.alveari, key=lambda alv: alv.produzione_totale(), default=None)


def main() -> None:
    # Creazione di un apicoltore
    apicoltore = Apicoltore(id_apicoltore="AP001", nome="Giuseppe Miele", numero_licenza="LIC2024001")

    # Creazione di sciami
    sciame1 = Sciame(id_sciame="S001", numero_api_stimato=50000, ha_regina=True)
    sciame2 = Sciame(id_sciame="S002", numero_api_stimato=45000, ha_regina=True)
    sciame3 = Sciame(id_sciame="S003", numero_api_stimato=30000, ha_regina=False)  # Sciame problematico

    # Creazione di alveari
    alveare1 = Alveare(
        id_alveare="ALV001", posizione_gps="45.464664, 9.188540", data_installazione=date(2024, 3, 15), sciame=sciame1
    )
    alveare2 = Alveare(
        id_alveare="ALV002", posizione_gps="45.465123, 9.189876", data_installazione=date(2024, 4, 10), sciame=sciame2
    )
    alveare3 = Alveare(  # Alveare con sciame problematico
        id_alveare="ALV003", posizione_gps="45.463987, 9.187234", data_installazione=date(2024, 2, 20), sciame=sciame3
    )

    # Aggiunta degli alveari all'apicoltore
    apicoltore.aggiungi_alveare(alveare1)
    apicoltore.aggiungi_alveare(alveare2)
    apicoltore.aggiungi_alveare(alveare3)

    # Registrazione di raccolte
    # Per alveare1
    apicoltore.registra_raccolta(
        alveare=alveare1,
        data_raccolta=date(2024, 5, 20),
        quantita_kg=25.5,
        tipo=TipoMiele.ACACIA,
        note="Ottima qualità, colore chiaro",
    )
    apicoltore.registra_raccolta(
        alveare=alveare1, data_raccolta=date(2024, 6, 15), quantita_kg=18.3, tipo=TipoMiele.TIGLIO, note="Aroma intenso"
    )

    # Per alveare2
    apicoltore.registra_raccolta(
        alveare=alveare2,
        data_raccolta=date(2024, 7, 1),
        quantita_kg=22.0,
        tipo=TipoMiele.MILLEFIORI,
        note="Mix di fiori di campo",
    )
    apicoltore.registra_raccolta(
        alveare=alveare2,
        data_raccolta=date(2024, 7, 25),
        quantita_kg=15.7,
        tipo=TipoMiele.CASTAGNO,
        note="Colore scuro, sapore forte",
    )
    # Aggiungiamo una raccolta di tipo ALTRO per test
    apicoltore.registra_raccolta(
        alveare=alveare2,
        data_raccolta=date(2024, 8, 5),
        quantita_kg=10.0,
        tipo=TipoMiele.ALTRO,
        note="Miele particolare",
    )

    # Alveare3 non ha raccolte, per simulare un alveare meno produttivo o nuovo

    # Visualizzazione dei risultati
    print(f"Sistema di Gestione Apiario - Report del {date.today()}")
    print("=" * 50)
    print(f"\nApicoltore: {apicoltore.nome}")
    print(f"Licenza: {apicoltore.numero_licenza}")
    print(f"Numero alveari gestiti: {len(apicoltore.alveari)}")

    print("\n--- Produzione Complessiva per Tipo di Miele ---")
    produzione = apicoltore.produzione_per_tipo()
    if any(q > 0 for q in produzione.values()):
        for tipo, quantita in produzione.items():
            if quantita > 0:  # Mostra solo i tipi con produzione
                print(f"  {tipo.value}: {quantita:.1f} kg")
    else:
        print("  Nessuna produzione registrata.")

    alveare_top = apicoltore.alveare_piu_produttivo()
    if alveare_top:
        print(f"\n--- Alveare Più Produttivo ---")
        print(f"  ID: {alveare_top.id_alveare}, Produzione: {alveare_top.produzione_totale():.1f} kg")
    else:
        print("\nNessun alveare registrato o nessuna produzione.")

    print("\n--- Dettagli Alveari ---")
    if not apicoltore.alveari:
        print("  Nessun alveare da mostrare.")
    for alveare in apicoltore.alveari:
        print(f"\n  Alveare ID: {alveare.id_alveare}")
        print(f"    Posizione GPS: {alveare.posizione_gps}")
        print(f"    Data Installazione: {alveare.data_installazione.strftime('%d/%m/%Y')}")
        print(f"    Età Alveare: {alveare.eta_giorni()} giorni")
        print(f"    Sciame ID: {alveare.sciame.id_sciame}")
        print(f"    Regina Presente: {'Sì' if alveare.sciame.ha_regina else 'No'}")
        print(f"    API Stimate: {alveare.sciame.numero_api_stimato:,}")
        print(f"    Produzione Totale: {alveare.produzione_totale():.1f} kg")
        print(f"    Numero Raccolte: {len(alveare.raccolte)}")
        print(f"    Media per Raccolta: {alveare.media_raccolte():.1f} kg")

        if alveare.raccolte:
            print("    Raccolte Effettuate:")
            for i, raccolta in enumerate(alveare.raccolte):
                print(
                    f"      {i + 1}. Data: {raccolta.data_raccolta.strftime('%d/%m/%Y')}, Tipo: {raccolta.tipo.value}, Quantità: {raccolta.quantita_kg:.1f} kg"
                )
                if raccolta.note:
                    print(f"         Note: {raccolta.note}")
        else:
            print("    Nessuna raccolta registrata per questo alveare.")

        # Identificazione alveari problematici (semplificata: sciame senza regina o produzione nulla nonostante età)
        problematico = False
        motivazioni = []
        if not alveare.sciame.ha_regina:
            problematico = True
            motivazioni.append("Sciame senza regina")
        if alveare.eta_giorni() > 60 and alveare.produzione_totale() == 0:  # Esempio: oltre 2 mesi e zero produzione
            problematico = True
            motivazioni.append("Nessuna produzione dopo un periodo significativo")

        if problematico:
            print(f"    ATTENZIONE: Alveare potenzialmente problematico ({', '.join(motivazioni)})")


if __name__ == "__main__":
    main()
