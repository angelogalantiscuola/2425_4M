# Esempio di utilizzo
if __name__ == "__main__":
    # Creare un corso
    corso_python = Corso("Corso Python", "Introduzione a Python", "Prof. Rossi")

    # Creare un quiz
    quiz = Quiz("Quiz Python Base", punteggioMinimo=1)

    # Aggiungere domande al quiz
    domanda1 = Domanda("Cosa è Python?", ["Un serpente", "Un linguaggio di programmazione", "Un gioco"], 1)
    quiz.domande.append(domanda1)

    # Impostare il quiz per il corso
    corso_python.impostaQuiz(quiz)

    # Creare uno studente
    studente = Studente("Mario", "Rossi", "mario.rossi@email.com")

    # Iscrivere lo studente al corso
    corso_python.iscriviStudente(studente)

    # Creare un tentativo di quiz
    tentativo_1 = QuizAttempt(quiz, studente)

    # Sottomettere le risposte
    tentativo_1.submitRisposte([0])  # Risposta corretta

    # Stampare i risultati
    print(f"Punteggio: {tentativo_1.punteggio}")
    print(f"Superato: {tentativo_1.superato}")

    # Creare un tentativo di quiz
    tentativo_2 = QuizAttempt(quiz, studente)

    # Sottomettere le risposte
    tentativo_2.submitRisposte([1])  # Risposta corretta

    # Stampare i risultati
    print(f"Punteggio: {tentativo_2.punteggio}")
    print(f"Superato: {tentativo_2.superato}")
