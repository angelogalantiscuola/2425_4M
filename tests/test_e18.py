import unittest
from src.e18 import Allenatore, Membro, Corso, SchedaAllenamento


class TestE18(unittest.TestCase):
    def setUp(self):
        self.allenatore1 = Allenatore("Giovanni", "Rossi", "Fitness")
        self.allenatore2 = Allenatore("Luca", "Bianchi", "Yoga")
        self.membro1 = Membro("Anna", "Verdi")
        self.membro2 = Membro("Marco", "Neri")
        self.corso1 = Corso("Pilates", "3 mesi", self.allenatore1)
        self.corso2 = Corso("HIIT", "6 mesi", self.allenatore1)
        self.corso3 = Corso("Yoga Avanzato", "4 mesi", self.allenatore2)
        self.scheda1 = SchedaAllenamento(
            self.membro1, ["Esercizio 1: Squat", "Esercizio 2: Push-up"]
        )
        self.scheda2 = SchedaAllenamento(
            self.membro2, ["Esercizio 1: Plank", "Esercizio 2: Burpee"]
        )

    def test_set_allenatore(self):
        self.membro1.set_allenatore(self.allenatore1)
        self.assertEqual(self.membro1.allenatore, self.allenatore1)
        self.assertIn(self.membro1, self.allenatore1.membri)

    def test_iscrivi_corso(self):
        self.membro1.iscrivi_corso(self.corso1)
        self.assertIn(self.corso1, self.membro1.corsi)
        self.assertIn(self.membro1, self.corso1.iscritti)

    def test_set_scheda_allenamento(self):
        self.membro1.set_scheda_allenamento(self.scheda1)
        self.assertEqual(self.membro1.scheda_allenamento, self.scheda1)
        self.assertEqual(self.scheda1.membro, self.membro1)

    def test_corso_allenatore_relationship(self):
        self.assertIn(self.corso1, self.allenatore1.corsi)
        self.assertEqual(self.corso1.allenatore, self.allenatore1)


if __name__ == "__main__":
    unittest.main()
