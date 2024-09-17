# Esercizio 01

Creare una classe `Auto` con i seguenti attributi: `marca`, `modello`, `targa`, `km_percorsi` e `stato`.

L'auto si rompe se ha più di 5 anni oppure più di 100.000 km percorsi. Questo stato deve essere rappresentato dall'attributo `stato`. L'attributo assume il valore `True` se l'auto è funzionante, altrimenti `False`.

Il costruttore `__init__()` deve permettere di istanziare un nuovo oggetto `Auto` con i valori specificati per questi attributi.

Inoltre, la classe deve avere un metodo `effettua_viaggio(km)` che aggiunge i chilometri specificati all'attributo `km_percorsi`.

La classe deve anche avere un metodo `incrementa_anno()` che incrementa l'anno di uno.

La classe deve avere un metodo `verifica_stato()` che restituisce lo `stato`.
