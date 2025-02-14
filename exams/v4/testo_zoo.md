# Esercizio - Sistema Gestione Zoo

Il sistema permette di gestire uno zoo moderno, inclusi animali, habitat, personale e visite veterinarie. Gli animali sono divisi in due categorie principali: **Mammiferi** e **Rettili**, ognuno con caratteristiche specifiche. Il sistema deve gestire anche gli habitat, e le visite veterinarie.

## Animale:

- codiceIdentificativo
- nome
- eta
- peso

### Mammifero

- tipoPelliccia
- temperaturaCorpo
- periodoGestazione

### Rettile

- velenoso (booleano)

## Habitat

- codiceArea
- nome
- dimensione

## Veterinario

- matricola
- nome
- cognome
- specializzazione
- anniEsperienza

## VisitaVeterinaria

- data
- diagnosi
- trattamentoProposto

## SistemaGestioneZoo

- Lista degli animali presenti
- Lista degli habitat
- Lista dei veterinari
- Registro delle visite veterinarie

## Il sistema deve implementare i seguenti metodi:

1. Aggiungere/rimuovere animali
2. Assegnare un animale a un habitat
3. Registrare una visita veterinaria
4. Visualizzare:
   - Tutti gli animali di un determinato habitat
   - Lo storico delle visite per un determinato animale
   - Età media degli animali per habitat

## Regole di Business:

1. Un animale può essere assegnato a un solo habitat alla volta
2. Gli animali della stessa specie devono essere nello stesso tipo di habitat: un animale puo essere assegnato ad un habitat se
   1. L'habitat e vuoto
   2. GLi animali dell'habitat hanno la stessa specie dell'animale

## Codice del Main

```python
def main():
    # Creazione del sistema
    zoo = SistemaGestioneZoo()

    # Creazione degli habitat
    savana = Habitat("H001", "Savana Africana", 1000.0)
    rettilario = Habitat("H002", "Rettilario", 500.0)
    zoo.habitats.extend([savana, rettilario])

    # Creazione dei veterinari
    vet1 = Veterinario("V001", "Mario", "Rossi", "Mammiferi", 10)
    vet2 = Veterinario("V002", "Laura", "Bianchi", "Rettili", 8)
    zoo.veterinari.extend([vet1, vet2])

    # Creazione degli animali
    leone = Mammifero("M001", "Simba", 5, 180.0, "Folta", 38.5, 110)
    serpente = Rettile("R001", "Kaa", 3, 5.0, True)
    giraffa = Mammifero("M002", "Melman", 7, 800.0, "Maculata", 38.0, 450)

    # Aggiunta degli animali al sistema
    for animale in [leone, serpente, giraffa]:
        zoo.aggiungi_animale(animale)

    # Assegnazione degli habitat
    zoo.assegna_habitat(leone, savana)
    zoo.assegna_habitat(giraffa, savana)
    success = zoo.assegna_habitat(serpente, savana)
    print("\nTentativo di mettere serpente in savana:", "Riuscito" if success else "Fallito")
    zoo.assegna_habitat(serpente, rettilario)

    # Effettuazione delle visite veterinarie
    visita1 = vet1.effettua_visita(leone, "Controllo di routine", "Somministrazione vaccino annuale")
    zoo.registra_visita(visita1)

    visita2 = vet2.effettua_visita(serpente, "Infezione batterica", "Antibiotico per 7 giorni")
    zoo.registra_visita(visita2)

    # Stampa delle informazioni
    print("\n=== Stato dello Zoo ===")

    print("\nAnimali nella Savana:")
    for animale in zoo.get_animali_habitat(savana):
        print(f"- {animale.nome} ({animale.codiceIdentificativo})")

    print("\nAnimali nel Rettilario:")
    for animale in zoo.get_animali_habitat(rettilario):
        print(f"- {animale.nome} ({animale.codiceIdentificativo})")

    print("\nEtà media per habitat:")
    for habitat, eta_media in zoo.calcola_eta_media_per_habitat().items():
        print(f"- {habitat}: {eta_media:.1f} anni")

    print("\nStorico visite di Simba:")
    for visita in zoo.get_storico_visite(leone):
        print(f"- Data: {visita.data}")
        print(f"  Veterinario: {visita.veterinario.nome} {visita.veterinario.cognome}")
        print(f"  Diagnosi: {visita.diagnosi}")
        print(f"  Trattamento: {visita.trattamentoProposto}")


if __name__ == "__main__":
    main()

# Tentativo di mettere serpente in savana: Fallito

# === Stato dello Zoo ===

# Animali nella Savana:
# - Simba (M001)
# - Melman (M002)

# Animali nel Rettilario:
# - Kaa (R001)

# Età media per habitat:
# - Savana Africana: 6.0 anni
# - Rettilario: 3.0 anni

# Storico visite di Simba:
# - Data: 2025-02-11 15:27:06.489484
#   Veterinario: Mario Rossi
#   Diagnosi: Controllo di routine
#   Trattamento: Somministrazione vaccino annuale

```
