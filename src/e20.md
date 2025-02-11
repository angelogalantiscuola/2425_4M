```mermaid
classDiagram

    class Prodotto {
        -int id
        -str nome 
        -str descrizione
        -float prezzo
        -str categoria
        +int get_id()
        +str get_nome()
        +float get_prezzo()
        +str get_categoria()
    }

    class OrdineProdotto {
        -Ordine ordine
        -Prodotto prodotto 
        -int quantita
        +Ordine get_ordine()
        +Prodotto get_prodotto()
        +int get_quantita()
    }

    class Ordine {
        -int id
        -date data_ordine
        -date data_consegna
        -str stato
        -Cliente cliente
        -list[OrdineProdotto] prodotti
        +int get_id()
        +tuple[date, date] get_date()
        +str get_stato()
        +Cliente get_cliente()
        +list[OrdineProdotto] get_prodotti()
    }
    class Cliente {
        -int id
        -str nome
        -str cognome
        -str email
        -str indirizzo
        +int get_id()
        +str get_nome_completo()
        +str get_email()
        +str get_indirizzo()
    }


    class Recensione {
        -int id
        -int punteggio
        -date data
        -str commento
        -Cliente cliente
        -Prodotto prodotto
        +int get_punteggio()
        +str get_commento()
        +Cliente get_cliente()
        +Prodotto get_prodotto()
    }

    Cliente "1" --> "*" Ordine : effettua
    Cliente "1" --> "*" Recensione : scrive
    Ordine "1" --> "*" OrdineProdotto : contiene
    Prodotto "1" <-- "*" OrdineProdotto : riferisce_a