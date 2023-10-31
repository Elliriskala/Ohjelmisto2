# Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti
# nollaksi. Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti
# "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
# Tämä tehdään kutsumalla kiihdytä-metodia. Kaikkia autoja käsketään liikkumaan yhden tunnin ajan.
# Tämä tehdään kutsumalla kulje-metodia. Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
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
        self.travelled += self.current_speed*hour
        print(f"{self.licenseplate} has travelled {self.travelled} km")


race_cars = []
for i in range(10):
    max_speed = random.randint(100, 200)
    race_car = max_speed
    licenseplate = f"ABC-{i+1}"
    race_car = Car(licenseplate, max_speed)
    race_cars.append(race_car)

for race_car in race_cars:
    race_car.new_car()

hour = 1
while True:
    print(f"Hour: {hour}")
    for race_car in race_cars:
        race_car.speed_up(random.randint(-10,15))
        race_car.car_travel(1)
    if not any(race_car.travelled >= 10000 for race_car in race_cars):
        hour += 1
        continue
    else:
        print("The race has ended.")
        break
print("*=======================================================================*")
print("The final scoreboard:")
for race_car in race_cars:
    print(f"Licenseplate: {race_car.licenseplate}, maxium speed: {race_car.max_speed} km/h, travelled distance: {race_car.travelled} km")
