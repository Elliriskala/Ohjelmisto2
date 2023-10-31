# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden
# muutoksen (km/h). Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion
# nopeus-ominaisuuden arvoa. Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
# Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
# Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
# Kuljettua matkaa ei tarvitse vielä päivittää.


class Car:

    def __init__(self, licenseplate, max_speed):
        self.licenseplate = licenseplate
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled = 0

    def new_car(self):
        print(f"The car's license plate is {self.licenseplate} and its maxium speed is {self.max_speed} km/h. "
              f"It has travelled {self.travelled} km and its current speed is {self.current_speed} km/h")

    def speed_up(self, current_speed):
        if self.current_speed + current_speed < 0:
            self.current_speed = 0
            print(f"You hit the brakes and now your current speed is {self.current_speed} km/h.")
            return
        if self.current_speed + current_speed > car1.max_speed:
            self.current_speed = car1.max_speed
            print(f"You are driving at your maxium speed {self.max_speed} km/h")
            return
        else:
            self.current_speed = self.current_speed + current_speed
        print(f"The car's current speed is {self.current_speed} km/h.")



car1 = Car("ABC-123", 142)
car1.new_car()

car1.speed_up(30)
car1.speed_up(70)
car1.speed_up(50)
car1.speed_up(-200)