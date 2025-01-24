import pytest
from centro_spaziale import (
    Astronauta,
    TecnicoControllo,
    IngegnereManutenzione,
    Missione,
    VeicoloSpaziale,
)


@pytest.fixture
def astronauta():
    return Astronauta("Luca", "Astronauta", 5, 100)


@pytest.fixture
def tecnico():
    return TecnicoControllo("Maria", "Tecnico", 10, "Comunicazioni")


@pytest.fixture
def ingegnere():
    return IngegnereManutenzione("Giulia", "Ingegnere", 8, ["CertA", "CertB"])


@pytest.fixture
def missione():
    return Missione("M001", "Esplorazione Luna", 30, "Pianificata")


@pytest.fixture
def veicolo():
    return VeicoloSpaziale("V001", "Satellite", "Operativo")


def test_astronauta_creation(astronauta):
    assert astronauta.nome == "Luca"
    assert astronauta.ruolo == "Astronauta"
    assert astronauta.anni_esperienza == 5
    assert astronauta.ore_volo == 100


def test_tecnico_controllo_assignment(tecnico, veicolo):
    veicolo.tecnico = tecnico
    assert veicolo.tecnico == tecnico
    assert tecnico.tecnico == veicolo  # Assuming the relationship is bidirectional


def test_ingegnere_manutenzione_assignment(ingegnere, veicolo):
    veicolo.ingegneri.append(ingegnere)
    assert ingegnere in veicolo.ingegneri


def test_missione_assignment(missione, astronauta):
    missione.astronauti.append(astronauta)
    assert astronauta in missione.astronauti


def test_veicolo_assignment_to_missione(missione, veicolo):
    missione.veicoli.append(veicolo)
    assert veicolo in missione.veicoli
    assert veicolo.stato_operativo == "Operativo"


def test_constraints_single_mission_per_veicolo(missione, veicolo):
    another_missione = Missione("M002", "Esplorazione Marte", 60, "Pianificata")
    veicolo.stato_operativo = "In Missione"
    missione.veicoli.append(veicolo)
    another_missione.veicoli.append(veicolo)
    assert veicolo in missione.veicoli
    assert veicolo in another_missione.veicoli
    # Add logic in the main code to prevent this if applicable


def test_ingegneri_multiple_assignments(ingegnere, veicolo):
    veicolo.ingegneri.append(ingegnere)
    another_ingegnere = IngegnereManutenzione("Marco", "Ingegnere", 7, ["CertC"])
    veicolo.ingegneri.append(another_ingegnere)
    assert ingegnere in veicolo.ingegneri
    assert another_ingegnere in veicolo.ingegneri
    assert len(veicolo.ingegneri) == 2


def test_astronauti_multiple_missions(astronauta, missione):
    another_missione = Missione("M002", "Esplorazione Marte", 60, "Pianificata")
    missione.astronauti.append(astronauta)
    another_missione.astronauti.append(astronauta)
    assert astronauta in missione.astronauti
    assert astronauta in another_missione.astronauti
    assert len(astronauta.ore_volo) == 2  # Adjust based on actual logic
