class PersonaleSpaziale:
    def __init__(self, nome: str, ruolo: str, anni_esperienza: int):
        self.nome = nome
        self.ruolo = ruolo
        self.anni_esperienza = anni_esperienza


class Astronauta(PersonaleSpaziale):
    def __init__(self, nome: str, ruolo: str, anni_esperienza: int, ore_volo: int):
        super().__init__(nome, ruolo, anni_esperienza)
        self.ore_volo = ore_volo
        self.missioni = []

    def assegnare_missione(self, missione):
        if missione not in self.missioni:
            self.missioni.append(missione)
            missione.astronauti.append(self)


class TecnicoControllo(PersonaleSpaziale):
    def __init__(self, nome: str, ruolo: str, anni_esperienza: int, specializzazione: str):
        super().__init__(nome, ruolo, anni_esperienza)
        self.specializzazione = specializzazione
        self.veicoli_supervisionati = []

    def assegnare_veicolo(self, veicolo):
        if veicolo.tecnico:
            veicolo.tecnico.veicoli_supervisionati.remove(veicolo)
        veicolo.tecnico = self
        self.veicoli_supervisionati.append(veicolo)


class IngegnereManutenzione(PersonaleSpaziale):
    def __init__(self, nome: str, ruolo: str, anni_esperienza: int, certificazioni: list):
        super().__init__(nome, ruolo, anni_esperienza)
        self.certificazioni = certificazioni
        self.veicoli_mantenuti = []

    def assegnare_veicolo_manutenzione(self, veicolo):
        if veicolo not in self.veicoli_mantenuti:
            self.veicoli_mantenuti.append(veicolo)
            veicolo.ingegneri.append(self)


class Missione:
    def __init__(self, codice: str, obiettivo: str, durata_giorni: int, stato: str):
        self.codice = codice
        self.obiettivo = obiettivo
        self.durata_giorni = durata_giorni
        self.stato = stato
        self.astronauti = []
        self.veicoli = []

    def aggiungi_veicolo(self, veicolo):
        if veicolo not in self.veicoli:
            if veicolo.stato_operativo == "Operativo":
                self.veicoli.append(veicolo)
                veicolo.stato_operativo = "In Missione"
            else:
                raise Exception("Veicolo non disponibile")

    def rimuovi_veicolo(self, veicolo):
        if veicolo in self.veicoli:
            self.veicoli.remove(veicolo)
            veicolo.stato_operativo = "Operativo"


class VeicoloSpaziale:
    def __init__(self, identificativo: str, tipo: str, stato_operativo: str):
        self.identificativo = identificativo
        self.tipo = tipo
        self.stato_operativo = stato_operativo
        self.tecnico = None
        self.ingegneri = []
        self.missione = None
        self.manutenzioni = []

    def assegnare_missione(self, missione):
        if self.missione is None:
            missione.aggiungi_veicolo(self)
            self.missione = missione
        else:
            raise Exception("Veicolo già assegnato a una missione")


class StatisticheCentroSpaziale:
    def __init__(self, personale: list):
        self.personale = personale

    def genera_report_missioni(self):
        report = []
        for persona in self.personale:
            if isinstance(persona, Astronauta):
                for missione in persona.missioni:
                    report.append(
                        {
                            "codice": missione.codice,
                            "obiettivo": missione.obiettivo,
                            "stato": missione.stato,
                            "numero_astronauti": len(missione.astronauti),
                            "numero_veicoli": len(missione.veicoli),
                        }
                    )
        return report

    def produce_statistiche_personale(self):
        stats = {
            "astronauti": len([p for p in self.personale if isinstance(p, Astronauta)]),
            "tecnici": len([p for p in self.personale if isinstance(p, TecnicoControllo)]),
            "ingegneri": len([p for p in self.personale if isinstance(p, IngegnereManutenzione)]),
        }
        return stats


def main():
    # Create personnel
    astro1 = Astronauta("Luca", "Astronauta", 5, 150)
    astro2 = Astronauta("Anna", "Astronauta", 3, 120)
    tecnico = TecnicoControllo("Maria", "Tecnico", 10, "Comunicazioni")
    ingegnere1 = IngegnereManutenzione("Giulia", "Ingegnere", 8, ["CertA", "CertB"])
    ingegnere2 = IngegnereManutenzione("Marco", "Ingegnere", 7, ["CertC"])

    # Create vehicles
    veicolo1 = VeicoloSpaziale("V001", "Satellite", "Operativo")
    veicolo2 = VeicoloSpaziale("V002", "Shuttle", "Operativo")

    # Create missions
    missione1 = Missione("M001", "Esplorazione Luna", 30, "Pianificata")
    missione2 = Missione("M002", "Esplorazione Marte", 60, "Pianificata")

    # Assign personnel to missions
    astro1.assegnare_missione(missione1)
    astro2.assegnare_missione(missione2)
    tecnico.assegnare_veicolo(veicolo1)
    ingegnere1.assegnare_veicolo_manutenzione(veicolo1)
    ingegnere2.assegnare_veicolo_manutenzione(veicolo2)

    # Assign vehicles to missions
    veicolo1.assegnare_missione(missione1)
    veicolo2.assegnare_missione(missione2)

    # Print missions
    print("Mission 1")
    print(missione1.codice)
    print(missione1.obiettivo)
    print(missione1.durata_giorni)
    print(missione1.stato)
    print(missione1.astronauti)
    print(missione1.veicoli)

    stats = StatisticheCentroSpaziale([astro1, astro2, tecnico, ingegnere1, ingegnere2])
    print(stats.genera_report_missioni())
    print(stats.produce_statistiche_personale())


if __name__ == "__main__":
    main()
