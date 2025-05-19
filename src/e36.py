from dataclasses import dataclass, field
from enum import Enum
from typing import List


class Direzione(Enum):
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"


class ClassePersonaggio(Enum):
    GUERRIERO = "GUERRIERO"
    MAGO = "MAGO"
    LADRO = "LADRO"


class TipoOggetto(Enum):
    POZIONE = "POZIONE"
    AMULETO = "AMULETO"
    CHIAVE = "CHIAVE"


@dataclass
class Oggetto:
    nome: str
    descrizione: str
    raccoglibile: bool
    tipo: TipoOggetto


@dataclass
class Stanza:
    nome_stanza: str
    descrizione: str
    stanza_aperta: bool
    stanza_up: "Stanza | None" = None
    stanza_down: "Stanza | None" = None
    stanza_left: "Stanza | None" = None
    stanza_right: "Stanza | None" = None
    oggetti: List[Oggetto] = field(default_factory=list)

    def descrivi_stanza(self) -> str:
        """Restituisce la descrizione della stanza."""
        return f"Stanza: {self.nome_stanza}\nDescrizione: {self.descrizione}"


@dataclass
class Personaggio:
    nome_personaggio: str
    classe_personaggio: ClassePersonaggio
    livello: int = 1
    punti_vita: int = 100
    stanza_corrente: Stanza | None = None
    inventario: List[Oggetto] = field(default_factory=list)

    def usa_oggetto(self, oggetto: Oggetto) -> bool:
        """Usa un oggetto dall'inventario."""
        if oggetto in self.inventario:
            self.inventario.remove(oggetto)
            print(f"{self.nome_personaggio} ha usato {oggetto.nome}")
            return True
        else:
            print(f"{oggetto.nome} non è nell'inventario di {self.nome_personaggio}")
            return False

    def raccogli_oggetto(self, oggetto: Oggetto) -> bool:
        """Raccoglie un oggetto dalla stanza corrente."""
        if self.stanza_corrente is None:
            print(f"{self.nome_personaggio} non è in nessuna stanza")
            return False
        if oggetto in self.stanza_corrente.oggetti:
            self.inventario.append(oggetto)
            self.stanza_corrente.oggetti.remove(oggetto)
            print(f"{self.nome_personaggio} ha raccolto {oggetto.nome}")
            return True
        else:
            print(f"{oggetto.nome} non è presente nella stanza corrente di {self.nome_personaggio}")
            return False

    def muovi(self, direzione: Direzione) -> bool:
        """Muove il personaggio nella direzione specificata."""
        if self.stanza_corrente is None:
            print(f"{self.nome_personaggio} non è in nessuna stanza")
            return False

        if direzione == Direzione.UP and self.stanza_corrente.stanza_up is not None:
            if not self.stanza_corrente.stanza_up.stanza_aperta:
                # controlla se nell'inventario c'è una chiave
                chiave_presente = False
                for oggetto in self.inventario:
                    if oggetto.tipo == TipoOggetto.CHIAVE:
                        chiave_presente = True
                        # rimuovi la chiave dall'inventario
                        self.inventario.remove(oggetto)
                        break
                if chiave_presente:
                    print(
                        f"{self.nome_personaggio} ha usato una chiave per aprire {self.stanza_corrente.stanza_up.nome_stanza}"
                    )
                    self.stanza_corrente.stanza_up.stanza_aperta = True
                    self.stanza_corrente = self.stanza_corrente.stanza_up
                    return True
                else:
                    # non può entrare nella stanza
                    print(
                        f"{self.nome_personaggio} non ha la chiave per entrare in {self.stanza_corrente.stanza_up.nome_stanza}"
                    )
                    return False
            else:
                self.stanza_corrente = self.stanza_corrente.stanza_up
        elif direzione == Direzione.DOWN and self.stanza_corrente.stanza_down:
            self.stanza_corrente = self.stanza_corrente.stanza_down
        elif direzione == Direzione.LEFT and self.stanza_corrente.stanza_left:
            self.stanza_corrente = self.stanza_corrente.stanza_left
        elif direzione == Direzione.RIGHT and self.stanza_corrente.stanza_right:
            self.stanza_corrente = self.stanza_corrente.stanza_right

        else:
            print(f"{self.nome_personaggio} non può muoversi in quella direzione")
            return False
        print(f"{self.nome_personaggio} si è spostato in {self.stanza_corrente.nome_stanza}")
        return True


#     def aggiungi_strumento(self, strumento: StrumentoVirtuale) -> None:
#         self.strumento_utilizzato = strumento
#         print(f"Aggiunto strumento {strumento.nome_strumento} alla traccia {self.nome_traccia}")

#     def applica_effetto(self, effetto: EffettoAudio) -> None:
#         self.effetti_applicati.append(effetto)
#         print(f"Applicato effetto {effetto.nome_effetto} alla traccia {self.nome_traccia}")

#     def rimuovi_effetto(self, effetto: EffettoAudio) -> None:
#         if effetto in self.effetti_applicati:
#             self.effetti_applicati.remove(effetto)
#             print(f"Rimosso effetto {effetto.nome_effetto} dalla traccia {self.nome_traccia}")

#     def imposta_sequenza_note(self, note: str) -> None:
#         self.sequenza_note_manuali = note
#         print(f"Note inserite nella traccia {self.nome_traccia}: {note}")

#     def reset(self) -> None:
#         """Resetta la traccia allo stato iniziale."""
#         self.durata_secondi = 0.0
#         self.volume_db = 0
#         self.sequenza_note_manuali = ""
#         self.effetti_applicati.clear()
#         print(f"Traccia {self.nome_traccia} resettata")

#     def modifica_volume(self, nuovo_volume_db: int) -> None:
#         self.volume_db = nuovo_volume_db
#         print(f"Volume della traccia {self.nome_traccia} impostato a {nuovo_volume_db}dB")

#     def ha_effetti(self) -> bool:
#         """Verifica se la traccia ha effetti audio applicati."""
#         return len(self.effetti_applicati) > 0


# @dataclass
# class ProgettoMusicale:
#     id_progetto: str
#     titolo_progetto: str
#     data_creazione: date
#     genere_musicale: str
#     tracce: List[TracciaAudio] = field(default_factory=list)

#     def aggiungi_traccia(self, nome_traccia: str, strumento: StrumentoVirtuale) -> TracciaAudio:
#         """Aggiunge una nuova traccia al progetto."""
#         traccia = TracciaAudio(id_traccia=generate_id("t"), nome_traccia=nome_traccia, strumento_utilizzato=strumento)
#         self.tracce.append(traccia)
#         print(f"Aggiunta nuova traccia '{nome_traccia}' al progetto '{self.titolo_progetto}'")
#         return traccia

#     def rimuovi_traccia(self, traccia: TracciaAudio) -> None:
#         """Rimuove una traccia dal progetto."""
#         if traccia in self.tracce:
#             self.tracce.remove(traccia)
#             print(f"Rimossa traccia '{traccia.nome_traccia}' dal progetto '{self.titolo_progetto}'")
#         else:
#             print(f"Traccia non trovata nel progetto '{self.titolo_progetto}'")

#     def modifica_genere(self, nuovo_genere: str) -> None:
#         """Modifica il genere musicale del progetto."""
#         self.genere_musicale = nuovo_genere
#         print(f"Genere del progetto '{self.titolo_progetto}' modificato in '{nuovo_genere}'")

#     def durata_totale(self) -> float:
#         """Calcola la durata totale del progetto in secondi."""
#         return sum(traccia.durata_secondi for traccia in self.tracce)

#     def percentuale_tracce_con_effetti(self) -> float:
#         """Calcola la percentuale di tracce che hanno almeno un effetto applicato."""
#         if not self.tracce:
#             return 0.0
#         tracce_con_effetti = 0
#         for traccia in self.tracce:
#             if traccia.ha_effetti():
#                 tracce_con_effetti += 1
#         return (tracce_con_effetti / len(self.tracce)) * 100

#     def effetto_piu_usato(self) -> Optional[TipoEffetto]:
#         """Identifica il tipo di effetto più frequentemente utilizzato nel progetto."""
#         effetti_count: Dict[TipoEffetto, int] = {
#             TipoEffetto.RIVERBERO: 0,
#             TipoEffetto.DELAY: 0,
#             TipoEffetto.DISTORSIONE: 0,
#         }

#         # Controlla ogni traccia e i suoi effetti
#         for traccia in self.tracce:
#             for effetto in traccia.effetti_applicati:
#                 tipo = effetto.tipo_effetto_audio
#                 effetti_count[tipo] += 1

#         # Trova il valore massimo
#         max_count = max(effetti_count.values())

#         # Trova il tipo di effetto con il conteggio massimo
#         for tipo, count in effetti_count.items():
#             if count == max_count:
#                 return tipo
#         return None


# @dataclass
# class Utente:
#     id_utente: str
#     nome_utente: str
#     email: str
#     progetti: List[ProgettoMusicale] = field(default_factory=list)

#     def crea_progetto(self, titolo: str, genere: str) -> ProgettoMusicale:
#         """Crea un nuovo progetto musicale."""
#         progetto = ProgettoMusicale(
#             id_progetto=generate_id("p"),
#             titolo_progetto=titolo,
#             data_creazione=date.today(),
#             genere_musicale=genere,
#         )
#         self.progetti.append(progetto)
#         print(f"Creato nuovo progetto '{titolo}' per l'utente {self.nome_utente}")
#         return progetto

#     def progetti_per_genere(self) -> Dict[str, int]:
#         """Restituisce un dizionario con il conteggio dei progetti per ogni genere musicale."""
#         generi_count: Dict[str, int] = {}
#         for progetto in self.progetti:
#             if progetto.genere_musicale in generi_count:
#                 generi_count[progetto.genere_musicale] += 1
#             else:
#                 generi_count[progetto.genere_musicale] = 1
#         return generi_count

#     def conta_progetti_totali(self) -> int:
#         """Calcola il numero totale di progetti dell'utente."""
#         return len(self.progetti)

#     def strumento_piu_usato(self) -> Optional[TipoStrumento]:
#         """Identifica lo strumento virtuale più utilizzato nei progetti dell'utente."""
#         strumenti_count: Dict[TipoStrumento, int] = {
#             TipoStrumento.BASSO: 0,
#             TipoStrumento.CHITARRA: 0,
#             TipoStrumento.BATTERIA: 0,
#         }
#         for progetto in self.progetti:
#             for traccia in progetto.tracce:
#                 tipo = traccia.strumento_utilizzato.tipo_strumento_virtuale
#                 strumenti_count[tipo] += 1

#         max_count = max(strumenti_count.values())

#         for tipo, count in strumenti_count.items():
#             if count == max_count:
#                 return tipo
#         return None


# # Esempio di utilizzo
# if __name__ == "__main__":
#     # Creazione utente
#     utente = Utente(generate_id("u"), "Mario Rossi", "mario@example.com")

#     # Creazione strumenti
#     basso = StrumentoVirtuale(generate_id("s"), "Basso elettrico", TipoStrumento.BASSO)
#     chitarra = StrumentoVirtuale(generate_id("s"), "Chitarra elettrica", TipoStrumento.CHITARRA)
#     batteria = StrumentoVirtuale(generate_id("s"), "Batteria acustica", TipoStrumento.BATTERIA)

#     # Creazione e gestione primo progetto (Rock)
#     progetto_rock = utente.crea_progetto("La Mia Canzone", "Rock")

#     traccia_basso = progetto_rock.aggiungi_traccia("Linea di basso", basso)
#     traccia_chitarra = progetto_rock.aggiungi_traccia("Chitarra ritmica", chitarra)

#     distorsione = EffettoAudio(generate_id("e"), "Distorsione Heavy", TipoEffetto.DISTORSIONE)
#     riverbero = EffettoAudio(generate_id("e"), "Riverbero Hall", TipoEffetto.RIVERBERO)

#     traccia_basso.applica_effetto(distorsione)
#     traccia_chitarra.applica_effetto(riverbero)

#     traccia_basso.modifica_volume(-6)
#     traccia_chitarra.modifica_volume(-3)

#     traccia_basso.imposta_sequenza_note("C2 G2 C3 E3")
#     traccia_chitarra.imposta_sequenza_note("E4 G4 B4")

#     # Creazione e gestione secondo progetto (Jazz)
#     progetto_jazz = utente.crea_progetto("Jazz Session", "Jazz")

#     traccia_basso_jazz = progetto_jazz.aggiungi_traccia("Bass groove", basso)
#     traccia_batteria = progetto_jazz.aggiungi_traccia("Drums", batteria)

#     delay = EffettoAudio(generate_id("e"), "Delay leggero", TipoEffetto.DELAY)
#     traccia_basso_jazz.applica_effetto(delay)

#     # Test dei metodi statistici
#     print("\nStatistiche utente:")
#     print(f"Totale progetti: {utente.conta_progetti_totali()}")
#     print(f"Progetti per genere: {utente.progetti_per_genere()}")
#     print(f"Strumento più usato: {utente.strumento_piu_usato()}")

#     print("\nStatistiche progetto Rock:")
#     print(f"Percentuale tracce con effetti: {progetto_rock.percentuale_tracce_con_effetti()}%")
#     print(f"Effetto più usato: {progetto_rock.effetto_piu_usato()}")

#     print("\nStatistiche tracce:")
#     print(f"Traccia basso ha effetti: {traccia_basso.ha_effetti()}")
