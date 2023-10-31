# Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
# Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös-
# tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen.
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat,
# missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten, että teet pääohjelmassa hissin
# ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

class Elevator:

    def __init__(self, lowest, highest):
        self.floor = lowest
        self.lowest_floor = lowest
        self.highest_floor = highest

    def floor_up(self):
        if self.floor < highest:
            self.floor = self.floor + 1
        print(f"You are now at floor: {self.floor}.")

    def floor_down(self):
        if self.floor > lowest:
            self.floor = self.floor - 1
        print(f"You are now at floor: {self.floor}.")

    def move_to_floor(self, floor):
        while self.floor != floor:
            if self.floor < floor:
                self.floor_up()

            else:
                self.floor_down()


print("You are now at floor: 1.")
user_input = int(input("Which floor you would like to go? "))

lowest = 1
highest = 10
floor = user_input
elevator = Elevator(lowest, highest)

elevator.move_to_floor(floor)

bottom = input("Type 'down' to go back to the lowest floor. ")
if bottom == 'down':
    elevator.move_to_floor(lowest)
