## Esercizio: Simulazione di Flotta Spaziale

### Prerequisiti

- Conoscenza di base della programmazione in Python.
- Comprensione delle classi e degli oggetti.
- Conoscenza dell'ereditarietà e del polimorfismo in Python.
- Comprensione dei metodi getter e setter.
- Familiarità con i magic methods (`__str__`) in Python.
- Familiarità con gli attributi e i metodi di classe.
- Familiarità con i metodi statici.

### Obiettivo

Creare una gerarchia di classi che rappresenti veicoli spaziali per l'esplorazione dell'universo.
Utilizzare l'ereditarietà per definire una classe base `VeicoloSpaziale` e classi derivate `Sonda`, `Astronave` e `StazioneOrbitante`.
Implementare metodi specifici per ogni tipo di veicolo e aggiungere funzionalità avanzate come:

- Conteggio totale dei veicoli creati.
- Simulazione di missioni spaziali con consumo di risorse e verifica del successo.
- Verifica della capacità di un'astronave di raggiungere una destinazione in base al carburante disponibile.
- Verifica della compatibilità di aggancio tra veicoli e gestione degli agganci.
- Calcolo del peso totale dei veicoli.
- Elenco dei veicoli agganciati a una stazione orbitante.
- Calcolo del tempo di comunicazione tra veicoli in base alla distanza.

### Istruzioni

#### 1. Classe Base `VeicoloSpaziale`:

- **Attributi Protetti:**

  - `_nome` (stringa): Nome del veicolo.
  - `_velocita_massima` (float, km/s): Velocità massima raggiungibile.
  - `_massa` (float, kg): Massa totale del veicolo.
  - `_posizione` (lista di float, km): Coordinate spaziali (x, y, z).

- **Attributi di Classe:**

  - `numero_veicoli` (intero): Conta il numero totale di veicoli creati.

- **Metodi:**

  - `__init__(...)`: Inizializza gli attributi dell'istanza e incrementa `numero_veicoli`.
  - **Getter e Setter** per ogni attributo.
  - `__str__()`: Restituisce una stringa descrittiva del veicolo.
  - `calcola_tempo_comunicazione(altro_veicolo)`:
    - Calcola il tempo necessario per comunicare con un altro veicolo.
    - **Calcoli Dettagliati:**
      - **Distanza tra i veicoli:**
        $
        \text{distanza} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}
        $
        (formula della distanza euclidea nello spazio tridimensionale)
      - **Tempo di comunicazione:**
        $
        \text{tempo} = \frac{\text{distanza}}{299792 \text{ km/s}}
        $
      - **Dove:** $ 299792 \text{ km/s} $ è la velocità della luce.

- **Metodo Statico `veicoli_totali()`:**
  - Restituisce `numero_veicoli`.

#### 2. Classe Derivata `Sonda`:

- Eredita da `VeicoloSpaziale`.

- **Attributi Aggiuntivi:**

  - `_tipo_missione` (stringa): Es. "Esplorazione", "Ricerca".
  - `_energia` (float, MJ): Energia disponibile per la missione.
  - `_consumo_energia` (float, MJ/h): Consumo energetico orario.

- **Metodi:**
  - **Getter e Setter** per i nuovi attributi.
  - `__str__()`: Estende il metodo per includere il tipo di missione e l'energia residua.
  - `simula_missione(durata)`:
    - Calcola il consumo totale di energia:
      $ \text{consumo} = \text{consumoenergia} \times \text{durata} $
    - **Verifica e Aggiornamento:**
      - Se `consumo` ≤ `_energia`:
        - Riduce `_energia` di `consumo`.
        - Restituisce `True` (missione completata con successo).
      - Altrimenti:
        - Restituisce `False` (energia insufficiente).

#### 3. Classe Derivata `Astronave`:

- Eredita da `VeicoloSpaziale`.

- **Attributi Aggiuntivi:**

  - `_numero_equipaggio` (intero): Numero di membri a bordo.
  - `_carburante` (float, tonnellate): Quantità di carburante disponibile.
  - `_consumo_carburante` (float, tonnellate/km): Consumo di carburante per chilometro.

- **Metodi:**
  - **Getter e Setter** per i nuovi attributi.
  - `__str__()`: Include informazioni sull'equipaggio e sul carburante.
  - `puo_raggiungere(distanza)`:
    - **Calcolo del Carburante Necessario:**
      $ \text{carburantenecessario} = \text{distanza} \times \text{consumocarburante} $
    - **Verifica della Disponibilità di Carburante:**
      - Se `carburante_necessario` ≤ `_carburante`:
        - Restituisce `True` (può raggiungere la destinazione).
      - Altrimenti:
        - Restituisce `False` (carburante insufficiente).

#### 4. Classe Derivata `StazioneOrbitante`:

- Eredita da `VeicoloSpaziale`.

- **Attributi Aggiuntivi:**

  - `_moduli` (lista di stringhe): Moduli che compongono la stazione.
  - `_capacita_aggancio` (intero): Numero massimo di veicoli agganciabili.
  - `_veicoli_agganciati` (lista di `VeicoloSpaziale`): Veicoli attualmente agganciati.

- **Metodi:**
  - **Getter e Setter** per i nuovi attributi.
  - `__str__()`: Include informazioni sui moduli e sugli agganci.
  - `aggancia_veicolo(veicolo)`:
    - **Verifica Capacità:**
      - Se la stazione ha capacita di aggancio:
        - Aggiunge `veicolo` a `_veicoli_agganciati`.
        - Restituisce `True` (aggancio riuscito).
      - Altrimenti:
        - Restituisce `False` (capacità massima raggiunta).
  - `sgancia_veicolo(veicolo)`:
    - **Rimozione del Veicolo:**
      - Se `veicolo` è in `_veicoli_agganciati`:
        - Rimuove `veicolo` da `_veicoli_agganciati`.
        - Restituisce `True` (sgancio riuscito).
      - Altrimenti:
        - Restituisce `False` (veicolo non trovato).
  - `elenca_veicoli_agganciati()`:
    - Restituisce una lista dei nomi dei veicoli attualmente agganciati.

#### 5. Funzioni Aggiuntive Esterne alle Classi:

- `calcola_peso_totale(veicoli)`:
  - Calcola la somma delle masse dei veicoli forniti.

### Programma Principale (Esempio di Utilizzo)

```python
sonda1 = Sonda(
    nome="Explorer I",
    velocita_massima=15,  # km/s
    massa=800,            # kg
    posizione=(1000, 2000, 3000),  # km
    tipo_missione="Ricerca",
    energia=5000,         # MJ
    consumo_energia=50    # MJ/h
)

astronave1 = Astronave(
    nome="Odyssey",
    velocita_massima=12,  # km/s
    massa=200000,         # kg
    posizione=(11500, 12500, 13500),  # km
    numero_equipaggio=100,
    carburante=600,       # tonnellate
    consumo_carburante=0.06  # tonnellate/km
)

stazione1 = StazioneOrbitante(
    nome="Alpha Station",
    velocita_massima=0,   # Stazionaria
    massa=500000,         # kg
    posizione=(0, 0, 0),  # km
    moduli=["Habitat", "Laboratorio", "Comunicazioni"],
    capacita_aggancio=2,
)

# Informazioni sui veicoli
print(sonda1)
print(astronave1)
print(stazione1)
# Sonda: Explorer I - Velocità Massima: 15 km/s - Massa: 800 kg - Missione: Ricerca - Energia: 5000 MJ
# Astronave: Odyssey - Velocità Massima: 12 km/s - Massa: 200000 kg - Equipaggio: 100 - Carburante: 600 t
# Stazione Orbitante: Alpha Station - Moduli: ['Habitat', 'Laboratorio', 'Comunicazioni'] - Capacità di Aggancio: 5 - Veicoli Agganciati: 0

# Simulazione di una missione con la sonda
durata_missione = 80  # ore
if sonda1.simula_missione(durata_missione):
    print("Missione completata con successo.")
else:
    print("Energia insufficiente per completare la missione.")
print(f"Energia residua della sonda: {sonda1.energia} MJ")
# Missione completata con successo.
# Energia residua della sonda: 1000 MJ

# Verifica se l'astronave può raggiungere una destinazione a 8000 km
distanza_destinazione = 8000  # km
if astronave1.puo_raggiungere(distanza_destinazione):
    print("L'astronave può raggiungere la destinazione.")
else:
    print("Carburante insufficiente per raggiungere la destinazione.")
# L'astronave può raggiungere la destinazione.


# Calcolo del tempo di comunicazione tra la sonda e l'astronave
tempo_comunicazione = sonda1.calcola_tempo_comunicazione(astronave1)
print(f"Tempo di comunicazione tra sonda e astronave: {tempo_comunicazione:.2f} s")
# Tempo di comunicazione tra sonda e astronave: 0.06 s


# Aggancio dell'astronave alla stazione
if stazione1.aggancia_veicolo(astronave1):
    print("Astronave agganciata con successo alla stazione.")
else:
    print("Capacità massima di aggancio raggiunta.")
# Astronave agganciata con successo alla stazione.


# Elenco dei veicoli agganciati
veicoli_agganciati = stazione1.elenca_veicoli_agganciati()
print(f"Veicoli agganciati alla stazione: {veicoli_agganciati}")
# Veicoli agganciati alla stazione: ['Odyssey']

# Calcolo del peso totale dei veicoli
veicoli = [sonda1, astronave1, stazione1]
peso_totale = calcola_peso_totale(veicoli)
print(f"Peso totale dei veicoli: {peso_totale} kg")
# Peso totale dei veicoli: 700800 kg

# Numero totale di veicoli creati
print(f"Numero totale di veicoli spaziali: {VeicoloSpaziale.veicoli_totali()}")
# Numero totale di veicoli spaziali: 3
```
