Realizza il diagramma UML e l'implementazione corrispondente della seguente situazione:
Si desidera sviluppare un software che modelli una rete di concessionari. Considera come possibili entità/classi `Veicolo/Vehicle`, `Cliente/Customer`, `Venditori/Salespeople`, `Showroom`, `Vendita/Sales`. Ricorda che ci possono essere più showroom e ognuno di essi ha più auto. Rappresenta le associazioni tra le classi. Usa l'ereditarietà per rappresentare i diversi tipi di veicolo.

Nella parte di logica implementativa:
Aggiungi delle liste che tengano traccia di tutte le istanze delle classi, come:
```python
# variabili di stato
salespersons = []
vehicles = []
sales = []
customers = []
showrooms = []
```

Nell'applicazione, implementa un menu di gestione del tipo:

1) Aggiungi showroom
2) Aggiungi venditore
3) Aggiungi veicolo
4) Effettua vendita
5) Mostra veicoli in vendita
6) Mostra vendite effettuate
7) Esci