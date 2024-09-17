# Crea una classe `Persona` e due classi che ereditano da essa: `Studente` e `Insegnante`.

In questo esercizio, `Persona` è la classe principale e `Studente` e `Insegnante` sono sottoclassi che ereditano da `Persona`.
Il metodo `presentati` viene sovrascritto nelle sottoclassi per fornire presentazioni diverse per studenti e insegnanti.

```python
studente = Studente("Giovanni", 15, 10)
print(studente.presentati())

insegnante = Insegnante("Gina", 30, "Matematica")
print(insegnante.presentati())
```
Output atteso:
```
Il mio nome è Giovanni e ho 15 anni. Sono uno studente del 10° grado.
Il mio nome è Gina e ho 30 anni. Insegno Matematica.
```