def main() -> None:
    # Creazione di un apicoltore
    apicoltore = Apicoltore(id_apicoltore="AP001", nome="Giuseppe Miele", numero_licenza="LIC2024001")

    # Creazione di sciami
    sciame1 = Sciame(id_sciame="S001", numero_api_stimato=50000, ha_regina=True)
    sciame2 = Sciame(id_sciame="S002", numero_api_stimato=45000, ha_regina=True)
    sciame3 = Sciame(id_sciame="S003", numero_api_stimato=30000, ha_regina=False)

    # Creazione di alveari
    alveare1 = Alveare(
        id_alveare="ALV001", posizione_gps="45.464664, 9.188540", data_installazione=date(2024, 3, 15), sciame=sciame1
    )
    alveare2 = Alveare(
        id_alveare="ALV002", posizione_gps="45.465123, 9.189876", data_installazione=date(2024, 4, 10), sciame=sciame2
    )
    alveare3 = Alveare(
        id_alveare="ALV003", posizione_gps="45.463987, 9.187234", data_installazione=date(2024, 2, 20), sciame=sciame3
    )

    # Aggiunta degli alveari all'apicoltore
    apicoltore.aggiungi_alveare(alveare1)
    apicoltore.aggiungi_alveare(alveare2)
    apicoltore.aggiungi_alveare(alveare3)

    # Registrazione di raccolte
    apicoltore.registra_raccolta(
        alveare=alveare1, quantita_kg=25.5, tipo=TipoMiele.ACACIA, note="Ottima qualità, colore chiaro"
    )
    apicoltore.registra_raccolta(alveare=alveare1, quantita_kg=18.3, tipo=TipoMiele.TIGLIO, note="Aroma intenso")
    apicoltore.registra_raccolta(
        alveare=alveare2, quantita_kg=22.0, tipo=TipoMiele.MILLEFIORI, note="Mix di fiori di campo"
    )
    apicoltore.registra_raccolta(
        alveare=alveare2, quantita_kg=15.7, tipo=TipoMiele.CASTAGNO, note="Colore scuro, sapore forte"
    )

    # Visualizzazione dei risultati
    print(f"\nApicoltore: {apicoltore.nome}")
    print(f"Licenza: {apicoltore.numero_licenza}")
    print(f"Numero alveari: {len(apicoltore.alveari)}")

    print("\nProduzione per tipo di miele:")
    produzione = apicoltore.produzione_per_tipo()
    for tipo, quantita in produzione.items():
        if quantita > 0:
            print(f"  {tipo.value}: {quantita:.1f} kg")

    alveare_top = apicoltore.alveare_piu_produttivo()
    if alveare_top:
        print(f"\nAlveare più produttivo: {alveare_top.id_alveare} ({alveare_top.produzione_totale():.1f} kg)")

    print("\\nDettagli alveari:")
    for alveare in apicoltore.alveari:
        print(f"\\n  {alveare.id_alveare}:")
        print(f"    Posizione: {alveare.posizione_gps}")
        print(f"    Regina presente: {'Sì' if alveare.sciame.ha_regina else 'No'}")
        print(f"    API stimate: {alveare.sciame.numero_api_stimato:,}")
        print(f"    Produzione totale: {alveare.produzione_totale():.1f} kg")
        print(f"    Media per raccolta: {alveare.media_raccolte():.1f} kg")
        print(f"    Età alveare: {alveare.eta_giorni()} giorni")


if __name__ == "__main__":
    main()
