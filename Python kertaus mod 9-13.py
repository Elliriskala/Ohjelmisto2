# virtuaalinen eläintarha

# Luokka = luokalla tarkoitetaan yleiskäsitettä, joka määrittää yleiset ja yhteiset piirteet, joita sen jäsenillä on.

# Alustaja = Olioiden luonnin helpottamiseksi luokan sisälle kirjoitetaan usein alustaja eli konstruktori,
# joka automaattisesti asettaa halutut arvot luotavan olion ominaisuuksiksi.

class Animals:

    # konstruktori, olioiden luonnin helpottamiseen tehty alustaja asettaa arvot luotavan olion ominaisuuksiksi
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    # luokan metodi eli funktio
    def make_sound(self):
        print(f"{self.species} {self.sound}")


# luodaan luokka eläintarha


class Zoo:

    # eläintarha ja eläin luokkien välillä pysyvä assosiaatiosuhde
    # yksisuuntainen assosiaatio = eläintarha on tietoinen eläimistä siellä, mutta eläin ei tiedä olevansa eläintarhassa
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.species} lisätty eläintarhaan")

    # olio voi käsitellä toisia olioita ja käsitellä niiden metodeja
    def all_animals(self):
        print(f"Tässä on kaikki eläintarhan eläimet ja niiden ääntäminen:")
        for animal in self.animals:
            animal.make_sound()


# Periytyminen
class Lintu(Animals):

    def __init__(self, species, sound, color):
        super().__init__(species, sound)
        self.color = color

    # metodin ylikirjoittaminen, eli nyt lisätään myös väri
    def make_sound(self):
        print(f"{self.species} {self.sound}")
        print(f"Linnun väri on: {self.color}")


# luodaan luokkien instansseja eli olioita

animal1 = Animals("Leijona", "karjuu")
animal1.make_sound()

animal2 = Animals("Tiikeri", "murisee")
animal2.make_sound()

animal3 = Animals("Koira", "haukkuu")
animal4 = Animals("Joutsen", "laulaa")

lintu1 = Lintu("Käki", "kukkuu", "ruskea")

# ASSOSIAATIO = Oliot voivat olla vuorovaikutuksessa keskenään: olio voi käsitellä toisia olioita
# ja kutsua niiden metodeja. Tätä olioiden välistä tuntemissuhdetta kutsutaan assosiaatioksi.

# pysyvä assosiaatio suhde = luokan sisällä olevan listan muistiin jäänyt suhde

# tilapäinen assosiaatinen suhde = luokka ei tallenna tietoa luokkien välisestä suhteesta

zoo = Zoo()
zoo.add_animal(animal1)
zoo.add_animal(animal2)
zoo.add_animal(animal3)
zoo.add_animal(animal4)
zoo.add_animal(lintu1)

zoo.all_animals()
