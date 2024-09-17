# Esercizio: Gestione di un Conto Bancario

Scrivi una classe `ContoBancario` che rappresenta un conto bancario. La classe deve avere i seguenti attributi e metodi:

## Attributi:
- `titolare` (pubblico): il nome del titolare del conto.
- `__saldo` (privato): il saldo del conto.

## Metodi:
- `__init__(self, titolare, saldo_iniziale)`: costruttore che inizializza il titolare e il saldo iniziale del conto.
- `deposita(self, importo)`: metodo pubblico che permette di depositare un importo nel conto.
- `preleva(self, importo)`: metodo pubblico che permette di prelevare un importo dal conto, se il saldo è sufficiente.
- `mostra_saldo(self)`: metodo pubblico che restituisce il saldo attuale del conto.

## Esempio di utilizzo:
```python
conto = ContoBancario("Alice", 1000)
conto.deposita(500)
conto.preleva(200)
print(f"Saldo attuale: {conto.mostra_saldo()}")  # Output: Saldo attuale: 1300
```