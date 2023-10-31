# Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi
# palohälytys, joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten,
# että talossasi tulee palohälytys.

class Elevator:

    def __init__(self, lowest, highest):
        self.floor = lowest
        self.lowest = lowest
        self.highest = highest

    def floor_up(self):
        if self.floor < self.highest:
            self.floor = self.floor + 1
        print(f"You are now at floor: {self.floor}.")

    def floor_down(self):
        if self.floor > lowest:
            self.floor = self.floor - 1
        print(f"You are now at floor: {self.floor}.")

    def move_to_floor(self, move_floor):
        while self.floor != move_floor:
            if self.floor < move_floor:
                self.floor_up()
            else:
                self.floor_down()


class House:

    def __init__(self, lowest, highest, number_of_elevators):
        self.floor = lowest
        self.lowest = lowest
        self.highest = highest
        self.elevators = [Elevator(lowest, highest) for _ in range(number_of_elevators)]

    def use_elevator(self, elevator_num, move_floor):
        if 1 <= elevator_num <= len(self.elevators):
            elevator = self.elevators[elevator_num -1]
            if move_floor > elevator.floor:
                elevator.move_to_floor(move_floor)
            elif move_floor < elevator.floor:
                elevator.move_to_floor(move_floor)
            print(f"You are now at floor number: {move_floor}.")

    def fire_alarm(self):
        print(f"The fire alarm of the building is going off.\n"
              f"All {number_of_elevators} elevators are going to the bottom floor.")
        for elevator in self.elevators:
            elevator.move_to_floor(lowest)
        print("Now all elevators are at the bottom floor.")



lowest = 1
highest = 10
number_of_elevators = 6

house = House(lowest, highest, number_of_elevators)

print("You are now at floor: 1.")

what_elevator = int(input("There are total of 6 elevators. Which one would you like to use? "))
print(f"You are now in elevator number: {what_elevator}")
use = int(input("Which floor you would like to go? "))
house.use_elevator(what_elevator, use)

print("Piip piiip piip!")
house.fire_alarm()
