# Esercizio 02

Creare una classe `ContoCorrente` con i seguenti attributi: `iban`, `intestatario`, `saldo_disponibile` e `portafoglio_investimenti`.

Il costruttore `__init__()` deve permettere di istanziare un nuovo oggetto `ContoCorrente` con i valori specificati per `iban`, `intestatario` e `saldo_disponibile`. L'attributo `portafoglio_investimenti` deve essere inizializzato a 0.

La classe deve avere un metodo `__str__()` che restituisce una stringa rappresentativa dell'oggetto `ContoCorrente`.

Inoltre, la classe deve avere i seguenti metodi:
- `deposita(importo)` che aggiunge l'importo specificato a `saldo_disponibile`.
- `preleva(importo)` che sottrae l'importo specificato da `saldo_disponibile` se sufficiente, altrimenti restituisce `False`.
- `investi(importo)` che trasferisce l'importo specificato da `saldo_disponibile` a `portafoglio_investimenti` se sufficiente, altrimenti restituisce `False`.
- `disinvesti(importo)` che trasferisce l'importo specificato da `portafoglio_investimenti` a `saldo_disponibile` se sufficiente, altrimenti restituisce `False`.
- `get_patrimonio_totale()` che restituisce la somma di `saldo_disponibile` e `portafoglio_investimenti`.
