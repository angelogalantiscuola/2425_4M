class VeicoloSpaziale:
    numero_veicoli = 0

    def __init__(self, nome, velocita_massima, massa, posizione):
        self._nome = nome
        self._velocita_massima = velocita_massima
        self._massa = massa
        self._posizione = posizione
        VeicoloSpaziale.numero_veicoli += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def velocita_massima(self):
        return self._velocita_massima

    @velocita_massima.setter
    def velocita_massima(self, velocita_massima):
        self._velocita_massima = velocita_massima

    @property
    def massa(self):
        return self._massa

    @massa.setter
    def massa(self, massa):
        self._massa = massa

    @property
    def posizione(self):
        return self._posizione

    @posizione.setter
    def posizione(self, posizione):
        self._posizione = posizione

    def __str__(self):
        return f"{self._nome} - Velocità Massima: {self._velocita_massima} km/s - Massa: {self._massa} kg"

    def calcola_tempo_comunicazione(self, altro_veicolo):
        distanza = (
            (self._posizione[0] - altro_veicolo.posizione[0]) ** 2
            + (self._posizione[1] - altro_veicolo.posizione[1]) ** 2
            + (self._posizione[2] - altro_veicolo.posizione[2]) ** 2
        ) ** 0.5
        tempo = distanza / 299792  # km/s
        return tempo

    @staticmethod
    def veicoli_totali():
        return VeicoloSpaziale.numero_veicoli


class Sonda(VeicoloSpaziale):
    def __init__(
        self,
        nome,
        velocita_massima,
        massa,
        posizione,
        tipo_missione,
        energia,
        consumo_energia,
    ):
        super().__init__(nome, velocita_massima, massa, posizione)
        self._tipo_missione = tipo_missione
        self._energia = energia
        self._consumo_energia = consumo_energia

    @property
    def tipo_missione(self):
        return self._tipo_missione

    @tipo_missione.setter
    def tipo_missione(self, tipo_missione):
        self._tipo_missione = tipo_missione

    @property
    def energia(self):
        return self._energia

    @energia.setter
    def energia(self, energia):
        self._energia = energia

    @property
    def consumo_energia(self):
        return self._consumo_energia

    @consumo_energia.setter
    def consumo_energia(self, consumo_energia):
        self._consumo_energia = consumo_energia

    def __str__(self):
        return super().__str__() + f" - Missione: {self._tipo_missione} - Energia: {self._energia} MJ"

    def simula_missione(self, durata):
        consumo = self._consumo_energia * durata
        if consumo <= self._energia:
            self._energia -= consumo
            return True
        else:
            return False


class Astronave(VeicoloSpaziale):
    def __init__(
        self,
        nome,
        velocita_massima,
        massa,
        posizione,
        numero_equipaggio,
        carburante,
        consumo_carburante,
    ):
        super().__init__(nome, velocita_massima, massa, posizione)
        self._numero_equipaggio = numero_equipaggio
        self._carburante = carburante
        self._consumo_carburante = consumo_carburante

    @property
    def numero_equipaggio(self):
        return self._numero_equipaggio

    @numero_equipaggio.setter
    def numero_equipaggio(self, numero_equipaggio):
        self._numero_equipaggio = numero_equipaggio

    @property
    def carburante(self):
        return self._carburante

    @carburante.setter
    def carburante(self, carburante):
        self._carburante = carburante

    @property
    def consumo_carburante(self):
        return self._consumo_carburante

    @consumo_carburante.setter
    def consumo_carburante(self, consumo_carburante):
        self._consumo_carburante = consumo_carburante

    def __str__(self):
        return super().__str__() + f" - Equipaggio: {self._numero_equipaggio} - Carburante: {self._carburante} t"

    def puo_raggiungere(self, distanza):
        carburante_necessario = distanza * self._consumo_carburante
        return carburante_necessario <= self._carburante


class StazioneOrbitante(VeicoloSpaziale):
    def __init__(self, nome, velocita_massima, massa, posizione, moduli, capacita_aggancio):
        super().__init__(nome, velocita_massima, massa, posizione)
        self._moduli = moduli
        self._capacita_aggancio = capacita_aggancio
        self._veicoli_agganciati = []

    @property
    def moduli(self):
        return self._moduli

    @moduli.setter
    def moduli(self, moduli):
        self._moduli = moduli

    @property
    def capacita_aggancio(self):
        return self._capacita_aggancio

    @capacita_aggancio.setter
    def capacita_aggancio(self, capacita_aggancio):
        self._capacita_aggancio = capacita_aggancio

    @property
    def veicoli_agganciati(self):
        return self._veicoli_agganciati

    def __str__(self):
        return super().__str__() + f" - Moduli: {self._moduli} - Capacità di Aggancio: {self._capacita_aggancio}"

    def aggancia_veicolo(self, veicolo):
        if len(self._veicoli_agganciati) < self._capacita_aggancio:
            self._veicoli_agganciati.append(veicolo)
            return True
        else:
            return False

    def sgancia_veicolo(self, veicolo):
        for v in self._veicoli_agganciati:
            if v.nome == veicolo.nome:
                self._veicoli_agganciati.remove(v)
                return True
        return False

    def elenca_veicoli_agganciati(self):
        return [veicolo.nome for veicolo in self._veicoli_agganciati]


def calcola_peso_totale(veicoli):
    return sum(veicolo.massa for veicolo in veicoli)


if __name__ == "__main__":
    sonda1 = Sonda(
        nome="Explorer I",
        velocita_massima=15,  # km/s
        massa=800,  # kg
        posizione=(1000, 2000, 3000),  # km
        tipo_missione="Ricerca",
        energia=5000,  # MJ
        consumo_energia=50,  # MJ/h
    )

    astronave1 = Astronave(
        nome="Odyssey",
        velocita_massima=12,  # km/s
        massa=200000,  # kg
        posizione=(11500, 12500, 13500),  # km
        numero_equipaggio=100,
        carburante=600,  # tonnellate
        consumo_carburante=0.06,  # tonnellate/km
    )

    stazione1 = StazioneOrbitante(
        nome="Alpha Station",
        velocita_massima=0,  # Stazionaria
        massa=500000,  # kg
        posizione=(0, 0, 0),  # km
        moduli=["Habitat", "Laboratorio", "Comunicazioni"],
        capacita_aggancio=2,
    )

    # Informazioni sui veicoli
    print(sonda1)
    print(astronave1)
    print(stazione1)

    # Simulazione di una missione con la sonda
    durata_missione = 80  # ore
    if sonda1.simula_missione(durata_missione):
        print("Missione completata con successo.")
    else:
        print("Energia insufficiente per completare la missione.")
    print(f"Energia residua della sonda: {sonda1.energia} MJ")

    # Verifica se l'astronave può raggiungere una destinazione a 8000 km
    distanza_destinazione = 8000  # km
    if astronave1.puo_raggiungere(distanza_destinazione):
        print("L'astronave può raggiungere la destinazione.")
    else:
        print("Carburante insufficiente per raggiungere la destinazione.")

    # Calcolo del tempo di comunicazione tra la sonda e l'astronave
    tempo_comunicazione = sonda1.calcola_tempo_comunicazione(astronave1)
    print(f"Tempo di comunicazione tra sonda e astronave: {tempo_comunicazione:.2f} s")

    # Aggancio dell'astronave alla stazione
    if stazione1.aggancia_veicolo(astronave1):
        print("Astronave agganciata con successo alla stazione.")
    else:
        print("Capacità massima di aggancio raggiunta.")

    # Elenco dei veicoli agganciati
    veicoli_agganciati = stazione1.elenca_veicoli_agganciati()
    print(f"Veicoli agganciati alla stazione: {veicoli_agganciati}")

    # Calcolo del peso totale dei veicoli
    veicoli = [sonda1, astronave1, stazione1]
    peso_totale = calcola_peso_totale(veicoli)
    print(f"Peso totale dei veicoli: {peso_totale} kg")

    # Numero totale di veicoli creati
    print(f"Numero totale di veicoli spaziali: {VeicoloSpaziale.veicoli_totali()}")
