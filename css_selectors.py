selectors = {
    "profil_zaufany": (
        "button.icon-button:nth-child(2)",
        {
            "mail": ".data-list > div:nth-child(1) > span:nth-child(1)",
            "tel": ".data-list > div:nth-child(2) > span:nth-child(1)",
        },
    ),
    "rejestr_danych_kontakotowych": (
        "button.icon-button:nth-child(3)",
        {
            "kontakt_tel": ".data-list > div:nth-child(1) > span:nth-child(1)",
            "kontakt_mail": ".data-list > div:nth-child(2) > span:nth-child(1)",
        },
    ),
    "rejestr_pesel": (
        "button.icon-button:nth-child(4)",
        {
            "imiona": "div.border-top-line:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)",
            "nazwisko": "div.border-top-line:nth-child(2) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)",
            "nazwisko_rodowe": "div.border-top-line:nth-child(2) > div:nth-child(2) > div:nth-child(3) > span:nth-child(1)",
            "stan_cywilny": "div.border-top-line:nth-child(2) > div:nth-child(2) > div:nth-child(4) > span:nth-child(1)",
            "data_urodzenia": "div.ng-star-inserted:nth-child(5) > span:nth-child(1)",
            "miejsce_urodzenia": "div.ng-star-inserted:nth-child(6) > span:nth-child(1)",
            "kraj_urodzenia": "div.ng-star-inserted:nth-child(7) > span:nth-child(1)",
            "oznaczenie_aktu_urodzenia": "div.ng-star-inserted:nth-child(8) > span:nth-child(1)",
            "urzad_wydajacy_akt": "div.ng-star-inserted:nth-child(9) > span:nth-child(1)",
            "plec": "div.ng-star-inserted:nth-child(10) > span:nth-child(1)",
            "pesel": "div.ng-star-inserted:nth-child(11) > span:nth-child(1)",
            "obywatelstwo": "div.ng-star-inserted:nth-child(12) > span:nth-child(1)",
            "imie_ojca": "div.border-top-line:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)",
            "nazwisko_rodowe_ojca": "div.border-top-line:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)",
            "imie_matki": "div.border-top-line:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(3) > span:nth-child(1)",
            "nazwisko_rodowe_matki": "div.border-top-line:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(4) > span:nth-child(1)",
        },
    ),
    "rejestr_dowodow_osobistych": (
        "button.icon-button:nth-child(5)",
        {
            "numer_dowodu_osobistego": "div.data-list:nth-child(3) > div:nth-child(1) > span:nth-child(1)",
            "organ_wydajacy": "div.data-list:nth-child(3) > div:nth-child(2) > span:nth-child(1)",
            "status_dowodu": "span.fw-bold",
            "data_waznosci_dowodu": "div.data-list:nth-child(3) > div:nth-child(5) > span:nth-child(1)",
            "status_warstwy_elektronicznej_dowodu": "div.ng-star-inserted:nth-child(6) > span:nth-child(1)",
        },
    ),
    "dane_zameldowania": (
        "button.icon-button:nth-child(6)",
        {
            "miejscowosc": ".data-list > div:nth-child(1) > span:nth-child(2)",
            "wojewodztwo": ".data-list > div:nth-child(2) > span:nth-child(2)",
            "powiat": ".data-list > div:nth-child(3) > span:nth-child(2)",
            "gmina": ".data-list > div:nth-child(4) > span:nth-child(2)",
            "kod_pocztowy": "div.ng-star-inserted:nth-child(5) > span:nth-child(2)",
            "ulica": "div.ng-star-inserted:nth-child(6) > span:nth-child(2)",
            "numer_domu": "div.ng-star-inserted:nth-child(7) > span:nth-child(2)",
            "numer_lokalu": "div.ng-star-inserted:nth-child(8) > span:nth-child(2)",
            "data_zameldowania_na_pobyt_staly": "div.ng-star-inserted:nth-child(9) > span:nth-child(2)",
        },
    ),
}
