# Esempio di utilizzo
if __name__ == "__main__":
    # Creazione utente
    utente = Utente("u1", "Mario Rossi", "mario@example.com")  # type: ignore # noqa: F821

    # Creazione progetto
    progetto = utente.crea_progetto("La Mia Canzone")

    # Aggiunta traccia
    traccia_basso = progetto.aggiungi_traccia("Linea di basso")

    # Creazione e aggiunta strumento
    basso = StrumentoVirtuale("s1", "Basso elettrico", TipoStrumento.BASSO)  # type: ignore # noqa: F821
    traccia_basso.aggiungi_strumento(basso)

    # Aggiunta effetti
    distorsione = EffettoAudio("e1", "Distorsione Heavy", TipoEffetto.DISTORSIONE)  # type: ignore # noqa: F821
    traccia_basso.applica_effetto(distorsione)

    # Impostazione volume
    traccia_basso.modifica_volume(-6)

    # Inserimento sequenza di note
    traccia_basso.imposta_sequenza_note("C2 G2 C3 E3")
