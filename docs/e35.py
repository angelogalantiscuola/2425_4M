# Esempio di utilizzo
if __name__ == "__main__":
    # Creazione utente
    utente = Utente("u1", "Mario Rossi", "mario@example.com")  # type: ignore # noqa: F821

    # Creazione progetti
    progetto_rock = utente.crea_progetto("La Mia Canzone Rock")
    progetto_rock.genere_musicale = "Rock"
    
    progetto_jazz = utente.crea_progetto("Jazz Session")
    progetto_jazz.genere_musicale = "Jazz"

    # Aggiunta tracce al progetto rock
    traccia_basso = progetto_rock.aggiungi_traccia("Linea di basso")
    traccia_chitarra = progetto_rock.aggiungi_traccia("Chitarra ritmica")

    # Creazione e aggiunta strumenti
    basso = StrumentoVirtuale("s1", "Basso elettrico", TipoStrumento.BASSO)  # type: ignore # noqa: F821
    chitarra = StrumentoVirtuale("s2", "Chitarra elettrica", TipoStrumento.CHITARRA)  # type: ignore # noqa: F821
    
    traccia_basso.aggiungi_strumento(basso)
    traccia_chitarra.aggiungi_strumento(chitarra)

    # Aggiunta effetti
    distorsione = EffettoAudio("e1", "Distorsione Heavy", TipoEffetto.DISTORSIONE)  # type: ignore # noqa: F821
    delay = EffettoAudio("e2", "Delay Echo", TipoEffetto.DELAY)  # type: ignore # noqa: F821
    
    traccia_basso.applica_effetto(distorsione)
    traccia_chitarra.applica_effetto(distorsione)
    traccia_chitarra.applica_effetto(delay)

    # Impostazione volume e note
    traccia_basso.modifica_volume(-6)
    traccia_basso.imposta_sequenza_note("C2 G2 C3 E3")
    traccia_chitarra.modifica_volume(-3)
    traccia_chitarra.imposta_sequenza_note("C4 G4 C5 E5 G5")

    # Test dei metodi statistici
    print("\nStatistiche a livello utente:")
    print(f"Progetti per genere: {utente.progetti_per_genere()}")
    print(f"Numero totali progetti: {utente.conta_progetti_totali()}")
    print(f"Strumento più usato: {utente.strumento_piu_usato().nome_strumento}")

    print("\nStatistiche progetto rock:")
    print(f"Percentuale tracce con effetti: {progetto_rock.percentuale_tracce_con_effetti()}%")
    print(f"Effetto più usato: {progetto_rock.effetto_piu_usato().nome_effetto}")

    print("\nStatistiche traccia basso:")
    print(f"Ha effetti: {traccia_basso.ha_effetti()}")
    print(f"Numero di note: {traccia_basso.numero_note()}")
