```mermaid
classDiagram
    class Animale {
        +str codice_microchip
        +str nome
        +int eta
        +str razza
        +datetime data_ingresso
        +bool registra_animale(codice_microchip, nome, eta, razza, data_ingresso)
    }

    class Visita_medica {
        +str tipologia
        +datetime data
        +str esito
    }

    class Vaccinazione {
        +datetime data_somministrazione
        +datetime data_scadenza
    }

    class Vaccino {
        +str nome
    }

    class Persona {
        +str cognome
        +str nome
        +str numero_di_telefono
    }

    class Canile {
        +str nome
        +str indirizzo
        +str numero_di_telefono
    }

    class Box {
        +int codice_area
        +int codice_identificativo
        +int larghezza
        +int lunghezza
        +bool libero
    }

    class Risorsa {
        +str tipologia
        +str nome_della_risorsa
        +int quantita
    }

    class Dipendente {
        +float stipendio
        +bool volontario
    }

    class Attivita {
        +str nome
    }


    Persona <|-- Dipendente
    Animale "*" -- "1" Persona : adotta
    Box "*" -- "1" Canile : ha
    Animale "0..1" -- "1" Box : si_trova_in     
    %% Animale "*" -- "1" Canile : si_trova_in     
    %% Persona "*" -- "1" Canile : visita
    Canile "1" -- "*" Risorsa : possiede
    Animale "1" -- "*" Visita_medica : effettua
    Animale "1" -- "*" Vaccinazione : riceve
    Vaccino "1" -- "*" Vaccinazione : riceve
    Dipendente "*" -- "*" Attivita : svolge