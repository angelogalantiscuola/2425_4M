from src.e17 import Insegnante, Studente, Corso  # type: ignore


def test_insegnante_attributes():
    insegnante = Insegnante("Mario", "Rossi", "Pianoforte")
    assert insegnante.nome == "Mario"
    assert insegnante.cognome == "Rossi"
    assert insegnante.strumento == "Pianoforte"
    assert insegnante.studenti == []


def test_studente_attributes():
    studente = Studente("Anna", "Verdi")
    assert studente.nome == "Anna"
    assert studente.cognome == "Verdi"
    assert studente.corsi == []
    assert studente.insegnante is None


def test_corso_attributes():
    corso = Corso("Teoria Musicale", "3 mesi")
    assert corso.nome == "Teoria Musicale"
    assert corso.durata == "3 mesi"
    assert corso.studenti == []


def test_assegna_insegnante_a_studente():
    insegnante = Insegnante("Mario", "Rossi", "Pianoforte")
    studente = Studente("Anna", "Verdi")

    studente.set_insegnante(insegnante)

    assert studente.insegnante == insegnante
    assert studente in insegnante.studenti


def test_iscrivi_studente_a_corso():
    studente = Studente("Anna", "Verdi")
    corso = Corso("Teoria Musicale", "3 mesi")

    studente.iscrivi_corso(corso)

    assert corso in studente.corsi
    assert studente in corso.studenti


def test_associazione_multiple():
    insegnante1 = Insegnante("Mario", "Rossi", "Pianoforte")
    insegnante2 = Insegnante("Luca", "Bianchi", "Chitarra")
    studente1 = Studente("Anna", "Verdi")
    studente2 = Studente("Marco", "Neri")
    corso1 = Corso("Teoria Musicale", "3 mesi")
    corso2 = Corso("Tecnica Pianistica", "6 mesi")

    studente1.set_insegnante(insegnante1)
    studente2.set_insegnante(insegnante2)
    studente1.iscrivi_corso(corso1)
    studente1.iscrivi_corso(corso2)
    studente2.iscrivi_corso(corso1)

    # Verifica associazioni per studente1
    assert corso1 in studente1.corsi
    assert corso2 in studente1.corsi
    assert studente1 in corso1.studenti
    assert studente1 in corso2.studenti

    # Verifica associazioni per studente2
    assert corso1 in studente2.corsi
    assert studente2 in corso1.studenti

    # Verifica insegnanti
    assert studente1.insegnante == insegnante1
    assert studente2.insegnante == insegnante2
    assert studente1 in insegnante1.studenti
    assert studente2 in insegnante2.studenti


def test_no_duplicate_association():
    studente = Studente("Anna", "Verdi")
    corso = Corso("Teoria Musicale", "3 mesi")

    studente.iscrivi_corso(corso)
    studente.iscrivi_corso(corso)  # Tentativo di aggiungere di nuovo lo stesso corso

    assert len(studente.corsi) == 1
    assert len(corso.studenti) == 1


def test_stampa_associazioni(capfd):
    insegnante1 = Insegnante("Mario", "Rossi", "Pianoforte")
    studente1 = Studente("Anna", "Verdi")
    studente2 = Studente("Marco", "Neri")
    corso1 = Corso("Teoria Musicale", "3 mesi")
    corso2 = Corso("Tecnica Pianistica", "6 mesi")

    studente1.set_insegnante(insegnante1)
    studente1.iscrivi_corso(corso1)
    studente1.iscrivi_corso(corso2)
    studente2.iscrivi_corso(corso1)

    # Funzione per stampare le associazioni
    print(f"{studente1.nome} {studente1.cognome} è iscritto ai seguenti corsi:")
    for corso in studente1.corsi:
        print(f"- {corso.nome} ({corso.durata})")

    print(f"\n{corso1.nome} ha i seguenti studenti iscritti:")
    for studente in corso1.studenti:
        print(f"- {studente.nome} {studente.cognome}")

    captured = capfd.readouterr()

    assert "Anna Verdi è iscritto ai seguenti corsi:" in captured.out
    assert "- Teoria Musicale (3 mesi)" in captured.out
    assert "- Tecnica Pianistica (6 mesi)" in captured.out
    assert "Teoria Musicale ha i seguenti studenti iscritti:" in captured.out
    assert "- Anna Verdi" in captured.out
    assert "- Marco Neri" in captured.out
