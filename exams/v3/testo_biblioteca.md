## Esercizio: Gestione di una biblioteca

Si desidera creare un sistema di gestione di una biblioteca, sulla gestione dei libri, degli autori e degli utenti. Il sistema deve includere diverse classi con i loro attributi e relazioni tra classi come associazioni e ereditarietà.

### Istruzioni

Creare un diagramma UML delle classi utilizzando la sintassi di MermaidJS. Consegnare un file markdown con il diagramma UML in un blocco mermaid.

Implementare il codice Python dell'esercizio utilizzando la programmazione orientata agli oggetti (OOP).

### Descrizione

In una biblioteca, ci sono libri, autori e utenti. Ogni libro ha un titolo, una data di pubblicazione e un autore. Ogni autore può scrivere più libri, ma ogni libro ha un solo autore.

Gli utenti della biblioteca hanno un nome, un cognome e una lista di libri che hanno preso in prestito. Un utente può prendere in prestito più libri e ogni libro può essere preso in prestito da più utenti, ma solo un utente alla volta può prendere in prestito un libro.

Inoltre, ogni libro ha una data di prestito e una data di restituzione.

La biblioteca è l'entità centrale che gestisce tutte le operazioni. Mantiene elenchi di:

- Libri disponibili
- Utenti registrati
- Autori nel catalogo

Operazioni principali della biblioteca

- Registrazione di nuovi libri e utenti
- Gestione dei prestiti
- Gestione delle restituzioni
- Verifica disponibilità libri
- Ricerca libri per titolo e per autore

### Main del programma

```python
def main():
    # Creazione biblioteca
    biblioteca = Biblioteca()

    # Creazione autori
    autore1 = Autore("Alessandro", "Manzoni")
    autore2 = Autore("Italo", "Calvino")

    # Creazione libri
    libro1 = Libro("I Promessi Sposi", date(1827, 1, 1), autore1)
    libro2 = Libro("Il barone rampante", date(1957, 1, 1), autore2)
    biblioteca.aggiungi_libro(libro1)
    biblioteca.aggiungi_libro(libro2)

    # Creazione utenti
    utente1 = Utente("Mario", "Rossi")
    utente2 = Utente("Laura", "Bianchi")
    biblioteca.aggiungi_utente(utente1)
    biblioteca.aggiungi_utente(utente2)

    # Test operazioni
    print("Libri disponibili:", [str(l) for l in biblioteca.libri_disponibili()])

    # Prestito libro
    biblioteca.presta_libro(libro1, utente1, date.today())
    print(f"\nLibro '{libro1}' prestato a {utente1}")

    # Verifica disponibilità
    print("\nLibri disponibili dopo il prestito:",
          [str(l) for l in biblioteca.libri_disponibili()])

    # Ricerca per autore
    print(f"\nLibri di {autore1}:",
          [str(l) for l in biblioteca.cerca_libri_per_autore(autore1)])

    # Restituzione libro
    biblioteca.restituisci_libro(libro1, date.today())
    print(f"\nLibro '{libro1}' restituito")

    print("\nLibri disponibili dopo la restituzione:",
          [str(l) for l in biblioteca.libri_disponibili()])

    # Ricerca libro per titolo
    libri_trovati = biblioteca.cerca_libro_per_titolo("Promessi")
    print(f"\nLibri trovati con titolo contenente 'Promessi':", [str(l) for l in libri_trovati])

    # Ottieni tutti i libri
    print("\nTutti i libri in biblioteca:", [str(l) for l in biblioteca.ottieni_libri()])

    # Ottieni tutti gli utenti
    print("\nTutti gli utenti in biblioteca:", [str(u) for u in biblioteca.ottieni_utenti()])

if __name__ == "__main__":
    main()

# Libri disponibili: ['I Promessi Sposi (Alessandro Manzoni)', 'Il barone rampante (Italo Calvino)']
# Libro 'I Promessi Sposi (Alessandro Manzoni)' prestato a Mario Rossi
# Libri disponibili dopo il prestito: ['Il barone rampante (Italo Calvino)']
# Libri di Alessandro Manzoni: ['I Promessi Sposi (Alessandro Manzoni)']
# Libro 'I Promessi Sposi (Alessandro Manzoni)' restituito
# Libri disponibili dopo la restituzione: ['I Promessi Sposi (Alessandro Manzoni)', 'Il barone rampante (Italo Calvino)']
# Libri trovati con titolo contenente 'Promessi': ['I Promessi Sposi (Alessandro Manzoni)']
# Tutti i libri in biblioteca: ['I Promessi Sposi (Alessandro Manzoni)', 'Il barone rampante (Italo Calvino)']
# Tutti gli utenti in biblioteca: ['Mario Rossi', 'Laura Bianchi']
```
