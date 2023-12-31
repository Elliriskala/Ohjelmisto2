# Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka,
# jolla on ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista.
# Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan
# ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:
#
# tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein
# tehtävät toimenpiteet eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle
# kulje-metodia. tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi
# taulukoksi muotoiltuna. kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa
# eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän. Muussa tapauksessa palautetaan
# False. Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
# Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
# Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia,
# jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi. Ajantasainen
# tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen
# sen jälkeen, kun kilpailu on päättynyt.

import random


class Car:

    def __init__(self, licenseplate, max_speed):
        self.licenseplate = licenseplate
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled = 0

    def new_car(self):
        print(f"The car's license plate is {self.licenseplate} and its maxium speed is {self.max_speed} km/h.")

    def speed_up(self, speed):
        if self.current_speed + speed < 0:
            self.current_speed = 0
            print(f"{self.licenseplate} hit the brakes and its current speed is {self.current_speed} km/h.")
        elif self.current_speed + speed > self.max_speed:
            self.current_speed = self.max_speed
            print(f"{self.licenseplate} is driving at its maxium speed {self.max_speed} km/h")
        else:
            self.current_speed = self.current_speed + speed
            print(f"{self.licenseplate} current speed is {self.current_speed} km/h.")

    def car_travel(self, hour):
        self.travelled += self.current_speed * hour
        print(f"{self.licenseplate} has travelled {self.travelled} km")


class Race:

    def __init__(self, name, race_len, race_cars):
        self.name = name
        self.race_len = race_len
        self.race_cars = race_cars

    def time(self):
        print(f"Hour: {hour}")
        for race_car in race_cars:
            race_car.speed_up(random.randint(-10, 15))
            race_car.car_travel(1)

    def status(self):
        print(f"Here is the status at hour {hour}: ")
        for race_car in race_cars:
            print(
                f"Licenseplate: {race_car.licenseplate}, maxium speed: {race_car.max_speed} km/h,"
                f" travelled distance: {race_car.travelled} km")

    def race_over(self):
        for race_car in self.race_cars:
            if race_car.travelled >= self.race_len:
                return True
        return False


hour = 0

race_cars = []
for i in range(10):
    max_speed = random.randint(100, 200)
    race_car = max_speed
    licenseplate = f"ABC-{i + 1}"
    race_car = Car(licenseplate, max_speed)
    race_cars.append(race_car)

for race_car in race_cars:
    race_car.new_car()

car_race = Race("Suuri romuralli", 8000, race_cars)

while not car_race.race_over():
    Race.time(1)
    hour += 1
    if hour % 10 == 0:
        Race.status(1)

print("*=======================================================================*")
print(f"The race 'Suuri Romuralli' has ended.")
car_race.status()
