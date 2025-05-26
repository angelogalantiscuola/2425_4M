def main() -> None:
    # Creazione di un utente
    utente: Utente = Utente(id_utente="U1", nome_utente="Mario Rossi", email="mario.rossi@email.com")

    # Creazione di due conti bancari
    conto_principale: ContoBancario = ContoBancario(id_conto="C1", nome_conto="Conto Principale", saldo_iniziale=1000.0)
    conto_risparmi: ContoBancario = ContoBancario(id_conto="C2", nome_conto="Conto Risparmi", saldo_iniziale=5000.0)

    # Aggiunta dei conti all'utente
    utente.conti.extend([conto_principale, conto_risparmi])

    # Registrazione di alcune transazioni
    utente.registra_transazione(
        conto=conto_principale, importo=-50.0, categoria=CategoriaSpesa.CIBO, descrizione="Spesa settimanale"
    )

    utente.registra_transazione(
        conto=conto_principale, importo=-30.0, categoria=CategoriaSpesa.TRASPORTI, descrizione="Benzina"
    )

    utente.registra_transazione(
        conto=conto_principale, importo=1000.0, categoria=CategoriaSpesa.ALTRO, descrizione="Stipendio"
    )

    utente.registra_transazione(
        conto=conto_risparmi, importo=-200.0, categoria=CategoriaSpesa.SVAGO, descrizione="Weekend fuori città"
    )

    # Visualizzazione dei risultati
    print(f"\nUtente: {utente.nome_utente}")
    print(f"Email: {utente.email}")

    for conto in utente.conti:
        print(f"\nConto: {conto.nome_conto}")
        print(f"Saldo disponibile: €{conto.saldo_disponibile():.2f}")
        print(f"Media spese totali: €{conto.media_spese_totali():.2f}")

    print("\nStatistiche spese:")
    spese: Dict[CategoriaSpesa, float] = utente.spese_per_categoria()
    for categoria, importo in spese.items():
        if importo > 0:
            print(f"{categoria.value}: €{importo:.2f}")

    categoria_max: CategoriaSpesa = utente.categoria_piu_costosa()
    print(f"\nCategoria più costosa: {categoria_max.value}")
    print(f"Totale spese mensili: €{utente.totale_spese_mensili():.2f}")


if __name__ == "__main__":
    main()
