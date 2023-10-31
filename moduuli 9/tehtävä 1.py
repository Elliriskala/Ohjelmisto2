# Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus
# ja kuljettu matka. Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua
# parametreina saatuihin arvoihin. Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
# Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class Car:

    def __init__(self, licenseplate, max_speed):
        self.licenseplate = licenseplate
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled = 0

    def new_car(self):
        print(f"The car's license plate is {self.licenseplate} and its maxium speed is {self.max_speed} km/h. "
              f"It has travelled {self.travelled} km and its current speed is {self.current_speed} km/h")

car1 = Car("ABC-123", 142)
car1.new_car()