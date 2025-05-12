class Superhero:
    def __init__(self, name, power, city):
        self.__name = name
        self.power = power
        self.city = city

    def show_info(self):
        print(f"{self.__name} protects {self.city} with {self.power}.")

    def use_power(self):
        print(f"{self.__name} uses {self.power}!")

class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    def use_power(self):
        print(f"{self.flight_speed} speed flight! Zoom!")

hero1 = Superhero("Shadow", "invisibility", "Gotham")
hero2 = FlyingHero("SkyFlash", "light speed", "Metropolis", "Mach 2")

hero1.show_info()
hero1.use_power()

hero2.show_info()
hero2.use_power()

class Vehicle:
    def move(self):
        print("Moving in a generic way.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
