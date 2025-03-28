### Esercizio di Verifica: Sistema di Gestione Ristorante in Python

#### Obiettivo

Creare un sistema di gestione per un ristorante utilizzando la programmazione orientata agli oggetti in Python. Il
sistema dovrà gestire il menu del ristorante (con primi e secondi piatti) e gli ordini associati ai tavoli.

#### Fase 1: Implementazione della Gerarchia dei Piatti

1. **Classe Base `ElementoMenu`**:

   - Implementare gli attributi: codice, nome, prezzo, tempo di preparazione, allergeni e disponibile
   - I metodi getter per accedere agli attributi
   - Il metodo `set_disponibile()` per modificare la disponibilità del piatto
   - Il metodo `to_string()` deve fornire una descrizione completa dell'elemento

2. **Classi Derivate**:
   - `PrimoPiatto`: gestisce il tipo di pasta e se è vegetariano
   - `SecondoPiatto`: gestisce la cottura predefinita
   - Ogni classe deve sovrascrivere il metodo `to_string()` per fornire una descrizione specifica

#### Fase 2: Gestione Ordini e Tavoli

1. **Classe `Ordine`**:

   - Implementare gli attributi: numero_ordine, data_ora, stato e elementi
   - Il metodo `calcola_totale()` deve sommare i prezzi di tutti gli elementi
   - I metodi `aggiungi_elemento()` e `rimuovi_elemento()` per gestire gli elementi nell'ordine
   - Gli stati possibili sono: "in_attesa", "in_preparazione", "pronto", "servito"

2. **Classe `Tavolo`**:
   - Implementare gli attributi: numero, posti e stato
   - Gestire lo stato del tavolo ("libero", "occupato")
   - Il metodo `is_libero()` deve verificare lo stato del tavolo
   - I metodi `aggiungi_ordine()` e `get_ordini_attivi()` per gestire gli ordini associati

#### Esempio di Utilizzo

```python
# Creazione elementi del menu
primo = PrimoPiatto("P1", "Spaghetti Carbonara", 12.0, 15, ["uova", "glutine"], True)
primo.set_tipo_pasta("spaghetti")
primo.set_vegetariano(False)

secondo = SecondoPiatto("S1", "Bistecca", 18.0, 20, [], True)
secondo.set_cottura_default("media")

# Creazione tavolo e ordine
tavolo = Tavolo(1, 4, "libero")
ordine = Ordine("ORD1", datetime.now(), "in_attesa", [])

# Aggiunta elementi all'ordine
ordine.aggiungi_elemento(primo)
ordine.aggiungi_elemento(secondo)

# Associazione ordine al tavolo
tavolo.aggiungi_ordine(ordine)
tavolo.set_stato("occupato")

# Calcoli
print(f"Totale ordine: {ordine.calcola_totale()}€")  # Output: Totale ordine: 30.0€

# Gestione stato ordine
ordine.set_stato("in_preparazione")
print(f"Stato ordine: {ordine.get_stato()}")  # Output: Stato ordine: in_preparazione

# Informazioni tavolo
print(f"Tavolo numero: {tavolo.get_numero()}")
print(f"Stato tavolo: {'libero' if tavolo.is_libero() else 'occupato'}")
print(f"Ordini attivi: {len(tavolo.get_ordini_attivi())}")
```

#### Requisiti di Implementazione

1. Utilizzare la sintassi Python per implementare classi e oggetti
2. Implementare tutti i getter e setter come mostrato nel diagramma UML
3. Gestire correttamente l'ereditarietà tra le classi
4. Implementare le associazioni tra classi come mostrato nel diagramma UML
5. Utilizzare tipi di dati appropriati per gli attributi
6. Implementare controlli di validità nei metodi quando necessario
7. Documentare il codice con docstring e commenti
