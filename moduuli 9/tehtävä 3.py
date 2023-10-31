# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5)
# kasvattaa kuljetun matkan lukemaan 2090 km.

class Car:

    def __init__(self, licenseplate, max_speed):
        self.licenseplate = licenseplate
        self.max_speed = max_speed
        self.current_speed = 60
        self.travelled = 2000

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

    def car_travel(self, hour):
        print(f"You have travelled {self.travelled + (self.current_speed*hour)} km")


car1 = Car("ABC-123", 142)
car1.new_car()

# car1.speed_up(30)
# car1.speed_up(70)
# car1.speed_up(50)
# car1.speed_up(-200)

car1.car_travel(1.5)