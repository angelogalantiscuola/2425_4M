import threading
import time
import random


class ContoBancario:
    def __init__(self, saldo_iniziale: int = 0) -> None:
        self.saldo: int = saldo_iniziale
        # Lock per gestire l'accesso concorrente al saldo
        self.lock: threading.Lock = threading.Lock()

    def deposito(self, importo: int) -> None:
        # Acquisisce il lock per garantire l'accesso esclusivo al saldo
        with self.lock:
            self.saldo += importo
            print(f"Deposito di {importo} effettuato. saldo attuale: {self.saldo}")

    def prelievo(self, importo: int) -> None:
        # Acquisisce il lock per garantire l'accesso esclusivo al saldo
        with self.lock:
            if self.saldo >= importo:
                self.saldo -= importo
                print(f"prelievo di {importo} effettuato. saldo attuale: {self.saldo}")
            else:
                print(f"prelievo di {importo} fallito. saldo insufficiente. saldo attuale: {self.saldo}")


# Definisce il tipo per le operazioni: una lista di tuple contenenti un'operazione e un importo
Operazione = dict[str, int]
Operazioni = list[Operazione]


# Funzione che verrà eseguita da ciascun thread
def operazioni_utente(conto: ContoBancario, operazioni: Operazioni) -> None:
    for operazione, importo in operazioni:
        # Aggiunge un ritardo casuale tra 0 e 3 secondi
        time.sleep(random.uniform(0, 3))
        if operazione == "deposito":
            conto.deposito(importo)
        elif operazione == "prelievo":
            conto.prelievo(importo)


if __name__ == "__main__":
    # Definizione delle operazioni per i due utenti
    operazioni_utente1: Operazioni = [
        {"deposito", 50},
        {"prelievo", 30},
        {"prelievo", 70},
    ]
    operazioni_utente2: Operazioni = [
        {"prelievo", 20},
        {"deposito", 100},
        {"prelievo", 50},
    ]

    print("=== Test con versione thread-safe (con lock) ===")
    conto_sicuro = ContoBancario(100)

    thread1: threading.Thread = threading.Thread(target=operazioni_utente, args=(conto_sicuro, operazioni_utente1))
    thread2: threading.Thread = threading.Thread(target=operazioni_utente, args=(conto_sicuro, operazioni_utente2))

    thread1.start()
    thread2.start()
    # Attende la terminazione dei due thread
    # I due thread eseguono operazioni in modo concorrente
    thread1.join()
    thread2.join()
    print(f"Saldo finale (versione sicura): {conto_sicuro.saldo}\n")
