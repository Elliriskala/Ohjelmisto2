# Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena
# on bensatankin koko litroina. Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa
# parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin. Se kutsuu yliluokan alustajaa
# kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa. Kirjoita pääohjelma,
# jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton
# (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan
# kolmen tunnin verran ja tulosta autojen matkamittarilukemat.

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


class Electric_car(Car):
    def __init__(self, licenseplate, max_speed, electric_kWh):
        self.electric_kWH = electric_kWh
        super().__init__(licenseplate, max_speed)

    def new_electric_car(self):
        super().new_car()
        print(f"The electric car consumes {self.electric_kWH} kW/h.")


class Diesel_car(Car):
    def __init__(self, licenseplate, max_speed, gasoline_l):
        self.gasoline_l = gasoline_l
        super().__init__(licenseplate, max_speed)

    def gasoline_car(self):
        super().new_car()
        print(f"The diesel car consumes {self.gasoline_l} l/h")


electric1 = Electric_car("ABC-15", 180, 52.5)
diesel1 = Diesel_car("ACD-123", 165, 32.3)

electric1.new_electric_car()
diesel1.gasoline_car()

print("*==================================================================*")

for i in range(3):
    electric1.speed_up(random.randint(40, 80))
    diesel1.speed_up(random.randint(40, 80))
    electric1.car_travel(1)
    diesel1.car_travel(1)

print("The race has ended.")

