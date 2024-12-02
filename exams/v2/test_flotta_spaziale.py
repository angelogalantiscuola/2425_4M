import pytest
from flotta_spaziale import (
    VeicoloSpaziale,
    Sonda,
    Astronave,
    StazioneOrbitante,
    calcola_peso_totale,
)


@pytest.fixture(autouse=True)
def reset_veicoli_totali():
    VeicoloSpaziale.numero_veicoli = 0


def test_veicolo_spaziale():
    veicolo = VeicoloSpaziale("Test", 10, 1000, (0, 0, 0))
    assert veicolo.nome == "Test"
    assert veicolo.velocita_massima == 10
    assert veicolo.massa == 1000
    assert veicolo.posizione == (0, 0, 0)
    assert VeicoloSpaziale.veicoli_totali() == 1


def test_veicolo_spaziale_str():
    veicolo = VeicoloSpaziale("Test", 10, 1000, (0, 0, 0))
    assert str(veicolo) == "Test - Velocità Massima: 10 km/s - Massa: 1000 kg"


def test_veicolo_spaziale_calcola_tempo_comunicazione():
    veicolo1 = VeicoloSpaziale("Veicolo1", 10, 1000, (0, 0, 0))
    veicolo2 = VeicoloSpaziale("Veicolo2", 10, 1000, (300000, 0, 0))
    assert veicolo1.calcola_tempo_comunicazione(veicolo2) == pytest.approx(1.0, rel=1e-2)


def test_sonda():
    sonda = Sonda("Sonda1", 15, 800, (1000, 2000, 3000), "Ricerca", 5000, 50)
    assert sonda.nome == "Sonda1"
    assert sonda.velocita_massima == 15
    assert sonda.massa == 800
    assert sonda.posizione == (1000, 2000, 3000)
    assert sonda.tipo_missione == "Ricerca"
    assert sonda.energia == 5000
    assert sonda.consumo_energia == 50


def test_sonda_str():
    sonda = Sonda("Sonda1", 15, 800, (1000, 2000, 3000), "Ricerca", 5000, 50)
    assert str(sonda) == "Sonda1 - Velocità Massima: 15 km/s - Massa: 800 kg - Missione: Ricerca - Energia: 5000 MJ"


def test_sonda_simula_missione():
    sonda = Sonda("Sonda1", 15, 800, (1000, 2000, 3000), "Ricerca", 5000, 50)
    assert sonda.simula_missione(80)
    assert sonda.energia == 1000
    assert not sonda.simula_missione(200)


def test_astronave():
    astronave = Astronave("Astronave1", 12, 200000, (1500, 2500, 3500), 100, 600, 0.06)
    assert astronave.nome == "Astronave1"
    assert astronave.velocita_massima == 12
    assert astronave.massa == 200000
    assert astronave.posizione == (1500, 2500, 3500)
    assert astronave.numero_equipaggio == 100
    assert astronave.carburante == 600
    assert astronave.consumo_carburante == 0.06


def test_astronave_str():
    astronave = Astronave("Astronave1", 12, 200000, (1500, 2500, 3500), 100, 600, 0.06)
    assert (
        str(astronave)
        == "Astronave1 - Velocità Massima: 12 km/s - Massa: 200000 kg - Equipaggio: 100 - Carburante: 600 t"
    )


def test_astronave_puo_raggiungere():
    astronave = Astronave("Astronave1", 12, 200000, (1500, 2500, 3500), 100, 600, 0.06)
    assert astronave.puo_raggiungere(8000)
    assert not astronave.puo_raggiungere(12000)


def test_stazione_orbitante():
    stazione = StazioneOrbitante("Stazione1", 0, 500000, (0, 0, 0), ["Habitat", "Laboratorio"], 5)
    assert stazione.nome == "Stazione1"
    assert stazione.velocita_massima == 0
    assert stazione.massa == 500000
    assert stazione.posizione == (0, 0, 0)
    assert stazione.moduli == ["Habitat", "Laboratorio"]
    assert stazione.capacita_aggancio == 5


def test_stazione_orbitante_str():
    stazione = StazioneOrbitante("Stazione1", 0, 500000, (0, 0, 0), ["Habitat", "Laboratorio"], 5)
    assert (
        str(stazione)
        == "Stazione1 - Velocità Massima: 0 km/s - Massa: 500000 kg - Moduli: ['Habitat', 'Laboratorio'] - Capacità di Aggancio: 5"
    )


def test_stazione_orbitante_aggancia_veicolo():
    stazione = StazioneOrbitante("Stazione1", 0, 500000, (0, 0, 0), ["Habitat", "Laboratorio"], 5)
    assert stazione.aggancia_veicolo(VeicoloSpaziale("Veicolo1", 10, 1000, (0, 0, 0)))
    assert stazione.aggancia_veicolo(VeicoloSpaziale("Veicolo2", 10, 1000, (0, 0, 0)))
    assert stazione.aggancia_veicolo(VeicoloSpaziale("Veicolo3", 10, 1000, (0, 0, 0)))
    assert stazione.aggancia_veicolo(VeicoloSpaziale("Veicolo4", 10, 1000, (0, 0, 0)))
    assert stazione.aggancia_veicolo(VeicoloSpaziale("Veicolo5", 10, 1000, (0, 0, 0)))
    assert stazione.elenca_veicoli_agganciati() == [
        "Veicolo1",
        "Veicolo2",
        "Veicolo3",
        "Veicolo4",
        "Veicolo5",
    ]


def test_stazione_orbitante_sgancia_veicolo():
    stazione = StazioneOrbitante("Stazione1", 0, 500000, (0, 0, 0), ["Habitat", "Laboratorio"], 5)
    stazione.aggancia_veicolo(VeicoloSpaziale("Veicolo1", 10, 1000, (0, 0, 0)))
    assert stazione.elenca_veicoli_agganciati() == ["Veicolo1"]
    assert stazione.sgancia_veicolo(VeicoloSpaziale("Veicolo1", 10, 1000, (0, 0, 0)))

    assert stazione.elenca_veicoli_agganciati() == []


def test_stazione_orbitante_aggancia_sgancia_veicolo():
    stazione = StazioneOrbitante("Stazione1", 0, 500000, (0, 0, 0), ["Habitat", "Laboratorio"], 1)
    veicolo = VeicoloSpaziale("Veicolo1", 10, 1000, (0, 0, 0))
    assert stazione.aggancia_veicolo(veicolo)
    assert stazione.elenca_veicoli_agganciati() == ["Veicolo1"]
    assert stazione.sgancia_veicolo(veicolo)
    assert stazione.elenca_veicoli_agganciati() == []


def test_stazione_orbitante_aggancia_oltre_capacita():
    stazione = StazioneOrbitante("Stazione1", 0, 500000, (0, 0, 0), ["Habitat", "Laboratorio"], 1)
    veicolo1 = VeicoloSpaziale("Veicolo1", 10, 1000, (0, 0, 0))
    veicolo2 = VeicoloSpaziale("Veicolo2", 10, 1000, (0, 0, 0))
    assert stazione.aggancia_veicolo(veicolo1)
    assert not stazione.aggancia_veicolo(veicolo2)


def test_calcola_peso_totale():
    veicoli = [
        VeicoloSpaziale("Veicolo1", 10, 1000, (0, 0, 0)),
        VeicoloSpaziale("Veicolo2", 10, 2000, (0, 0, 0)),
        VeicoloSpaziale("Veicolo3", 10, 3000, (0, 0, 0)),
    ]
    assert calcola_peso_totale(veicoli) == 6000


def test_calcola_peso_totale_vuoto():
    veicoli = []
    assert calcola_peso_totale(veicoli) == 0


def test_calcola_peso_totale_un_veicolo():
    veicoli = [VeicoloSpaziale("Veicolo1", 10, 1000, (0, 0, 0))]
    assert calcola_peso_totale(veicoli) == 1000
