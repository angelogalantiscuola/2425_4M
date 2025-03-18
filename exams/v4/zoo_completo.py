from datetime import datetime


class Animale:
    def __init__(self, codice: str, nome: str, eta: int, peso: float):
        self.codiceIdentificativo = codice
        self.nome = nome
        self.eta = eta
        self.peso = peso
        self.habitat_corrente: "Habitat" = None
        self.storico_visite = []

    def aggiungi_visita(self, visita) -> None:
        self.storico_visite.append(visita)


class Mammifero(Animale):
    def __init__(
        self,
        codice: str,
        nome: str,
        eta: int,
        peso: float,
        tipo_pelliccia: str,
        temperatura_corpo: float,
        periodo_gestazione: int,
    ):
        super().__init__(codice, nome, eta, peso)
        self.tipoPelliccia = tipo_pelliccia
        self.temperaturaCorpo = temperatura_corpo
        self.periodoGestazione = periodo_gestazione


class Rettile(Animale):
    def __init__(self, codice: str, nome: str, eta: int, peso: float, velenoso: bool):
        super().__init__(codice, nome, eta, peso)
        self.velenoso = velenoso


class Habitat:
    def __init__(self, codice: str, nome: str, dimensione: float):
        self.codiceArea = codice
        self.nome = nome
        self.dimensione = dimensione
        self.animali: list[Animale] = []

    def aggiungi_animale(self, animale: Animale) -> None:
        if animale not in self.animali:
            self.animali.append(animale)
            animale.habitat_corrente = self

    def rimuovi_animale(self, animale: Animale) -> None:
        if animale in self.animali:
            self.animali.remove(animale)
            animale.habitat_corrente = None

    def get_animali(self) -> list[Animale]:
        return self.animali.copy()

    def get_eta_media(self) -> float:
        if not self.animali:
            return 0.0
        return sum(a.eta for a in self.animali) / len(self.animali)


class Veterinario:
    def __init__(self, matricola: str, nome: str, cognome: str, specializzazione: str, anni_esperienza: int):
        self.matricola = matricola
        self.nome = nome
        self.cognome = cognome
        self.specializzazione = specializzazione
        self.anniEsperienza = anni_esperienza

    def effettua_visita(self, animale: Animale, diagnosi: str, trattamento: str) -> "VisitaVeterinaria":
        visita = VisitaVeterinaria(datetime.now(), diagnosi, trattamento, self, animale)
        animale.aggiungi_visita(visita)
        return visita


class VisitaVeterinaria:
    def __init__(self, data: datetime, diagnosi: str, trattamento: str, veterinario: Veterinario, animale: Animale):
        self.data = data
        self.diagnosi = diagnosi
        self.trattamentoProposto = trattamento
        self.veterinario = veterinario
        self.animale = animale


class SistemaGestioneZoo:
    def __init__(self):
        self.animali: list[Animale] = []
        self.habitats: list[Habitat] = []
        self.veterinari: list[Veterinario] = []
        self.visite: list[VisitaVeterinaria] = []

    def aggiungi_animale(self, animale: Animale) -> None:
        if animale not in self.animali:
            self.animali.append(animale)

    def rimuovi_animale(self, animale: Animale) -> None:
        if animale in self.animali:
            if animale.habitat_corrente:
                animale.habitat_corrente.rimuovi_animale(animale)
            self.animali.remove(animale)

    def assegna_habitat(self, animale: Animale, habitat: Habitat) -> bool:
        # Verifica che l'habitat sia compatibile con il tipo di animale
        habitat_compatibili = self.get_habitat_compatibili(animale)
        if habitat not in habitat_compatibili:
            return False

        # Rimuovi l'animale dall'habitat corrente se presente
        if animale.habitat_corrente:
            animale.habitat_corrente.rimuovi_animale(animale)

        # Assegna il nuovo habitat
        habitat.aggiungi_animale(animale)
        return True

    def registra_visita(self, visita: VisitaVeterinaria) -> None:
        self.visite.append(visita)

    def get_animali_habitat(self, habitat: Habitat) -> list[Animale]:
        return habitat.get_animali()

    def get_storico_visite(self, animale: Animale) -> list[VisitaVeterinaria]:
        return animale.storico_visite

    def get_habitat_compatibili(self, animale: Animale) -> list[Habitat]:
        # Trova habitat con animali dello stesso tipo
        tipo_animale = type(animale)
        habitat_compatibili = []

        for habitat in self.habitats:
            # Se l'habitat è vuoto, è compatibile
            if not habitat.animali:
                habitat_compatibili.append(habitat)
            # Se contiene animali dello stesso tipo, è compatibile
            else:
                for a in habitat.animali:
                    if type(a) is tipo_animale:
                        habitat_compatibili.append(habitat)

        return habitat_compatibili

    def calcola_eta_media_per_habitat(self) -> dict[str, float]:
        eta_media_per_habitat = {}
        for habitat in self.habitats:
            eta_media_per_habitat[habitat.nome] = habitat.get_eta_media()
        return eta_media_per_habitat


def main():
    # Creazione del sistema
    zoo = SistemaGestioneZoo()

    # Creazione degli habitat
    savana = Habitat("H001", "Savana Africana", 1000.0)
    rettilario = Habitat("H002", "Rettilario", 500.0)
    zoo.habitats.extend([savana, rettilario])

    # Creazione dei veterinari
    vet1 = Veterinario("V001", "Mario", "Rossi", "Mammiferi", 10)
    vet2 = Veterinario("V002", "Laura", "Bianchi", "Rettili", 8)
    zoo.veterinari.extend([vet1, vet2])

    # Creazione degli animali
    leone = Mammifero("M001", "Simba", 5, 180.0, "Folta", 38.5, 110)
    serpente = Rettile("R001", "Kaa", 3, 5.0, True)
    giraffa = Mammifero("M002", "Melman", 7, 800.0, "Maculata", 38.0, 450)

    # Aggiunta degli animali al sistema
    for animale in [leone, serpente, giraffa]:
        zoo.aggiungi_animale(animale)

    # Assegnazione degli habitat
    zoo.assegna_habitat(leone, savana)
    zoo.assegna_habitat(giraffa, savana)
    success = zoo.assegna_habitat(serpente, savana)
    print("\nTentativo di mettere serpente in savana:", "Riuscito" if success else "Fallito")
    zoo.assegna_habitat(serpente, rettilario)

    # Effettuazione delle visite veterinarie
    visita1 = vet1.effettua_visita(leone, "Controllo di routine", "Somministrazione vaccino annuale")
    zoo.registra_visita(visita1)

    visita2 = vet2.effettua_visita(serpente, "Infezione batterica", "Antibiotico per 7 giorni")
    zoo.registra_visita(visita2)

    # Stampa delle informazioni
    print("\n=== Stato dello Zoo ===")

    print("\nAnimali nella Savana:")
    for animale in zoo.get_animali_habitat(savana):
        print(f"- {animale.nome} ({animale.codiceIdentificativo})")

    print("\nAnimali nel Rettilario:")
    for animale in zoo.get_animali_habitat(rettilario):
        print(f"- {animale.nome} ({animale.codiceIdentificativo})")

    print("\nEtà media per habitat:")
    for habitat, eta_media in zoo.calcola_eta_media_per_habitat().items():
        print(f"- {habitat}: {eta_media:.1f} anni")

    print("\nStorico visite di Simba:")
    for visita in zoo.get_storico_visite(leone):
        print(f"- Data: {visita.data}")
        print(f"  Veterinario: {visita.veterinario.nome} {visita.veterinario.cognome}")
        print(f"  Diagnosi: {visita.diagnosi}")
        print(f"  Trattamento: {visita.trattamentoProposto}")


if __name__ == "__main__":
    main()

# Tentativo di mettere serpente in savana: Fallito

# === Stato dello Zoo ===

# Animali nella Savana:
# - Simba (M001)
# - Melman (M002)

# Animali nel Rettilario:
# - Kaa (R001)

# Età media per habitat:
# - Savana Africana: 6.0 anni
# - Rettilario: 3.0 anni

# Storico visite di Simba:
# - Data: 2025-02-11 15:27:06.489484
#   Veterinario: Mario Rossi
#   Diagnosi: Controllo di routine
#   Trattamento: Somministrazione vaccino annuale
