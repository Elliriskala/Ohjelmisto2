# Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti.
# Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja.
# Kirjoita luokkiin myös tarvittavat alustajat. Tee aliluokkiin metodi tulosta_tiedot,
# joka tudostaa kyseisen julkaisun kaikki tiedot. Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä)
# ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
# Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def julkaisun_nimi(self):
        print(f"Julkaisun nimi on {self.nimi}.")


class Lehti(Julkaisu):
    def __init__(self, nimi, toimittaja):
        self.toimittaja = toimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().julkaisun_nimi()
        print(f"Lehden toimittaja on {self.toimittaja}.")


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivut):
        self.kirjoittaja = kirjoittaja
        self.sivut = sivut
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().julkaisun_nimi()
        print(f"Kirjan kirjoittaja on {self.kirjoittaja} ja kirjassa on {self.sivut} sivua.")


lehti1 = Lehti("Aku Ankka", "Aki Hyyppä")
lehti1.tulosta_tiedot()

kirja1 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
kirja1.tulosta_tiedot()