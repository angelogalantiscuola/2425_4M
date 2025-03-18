class Studente:
    def __init__(self, nome: str):
        self.nome = nome
        self.corsi = []

class Quiz:
    def __init__(self, nome: str):
        self.nome = nome
        self.domande = []

    def aggiungiDomanda(self: 'Quiz', domanda: 'Domanda') -> None:
        self.domande.append(domanda)

class Domanda:
    def __init__(self, testo: str, opzioni: list[str], risposta_corretta: int):
        self.testo = testo
        self.opzioni = opzioni
        self.rispostaCorretta = risposta_corretta

class Corso:
    def __init__(self, titolo: str, descrizione: str, docente: str):
        self.titolo = titolo
        self.descrizione = descrizione
        self.docente = docente
        self.quiz = None
        self.studenti: list[Studente] = []

    def aggiungiStudente(self: 'Corso', studente: Studente) -> None:
        self.studenti.append(studente)
        studente.corsi.append(self)
        
    def aggiungiQuiz(self, quiz: 'Quiz') -> None:
        self.quiz = quiz


# Esempio di utilizzo
if __name__ == "__main__":
    # Creare un corso
    corso_python = Corso(
        titolo = "Corso Python", 
        descrizione = "Introduzione a Python", 
        docente = "Prof. Rossi")

    # Creare un quiz
    quiz = Quiz("Quiz Python Base")

    # Aggiungere domande al quiz
    domanda1 = Domanda(
        testo = "Cosa è Python?", 
        opzioni = ["Un serpente", "Un linguaggio di programmazione", "Un gioco"],
         risposta_corretta=1)
    
    quiz.aggiungiDomanda(domanda1)

    # Impostare il quiz per il corso
    corso_python.aggiungiQuiz(quiz)

    # Creare uno studente
    studente = Studente("Mario")

    corso_python.aggiungiStudente(studente)

    # print studenti del corso
    print(f"Studenti del corso {corso_python.titolo}:")
    for studente in corso_python.studenti:
        print(studente.nome)
    print()
    
    # print le domande del quiz
    for domanda in quiz.domande:
        print(domanda.testo)
        # for i, opzione in enumerate(domanda.opzioni):
        #     print(f"{i+1}. {opzione}")
        for opzione in domanda.opzioni:
            print(opzione)
        print()
