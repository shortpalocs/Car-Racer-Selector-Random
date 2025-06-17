import random
import time, os














caremoji = ["🚗", "🏎️", "🚙", "🚐", "🚓"]
randommake = ["Ford", "Lamborghini", "Bugatti", "Porsche", "Toyota", "BMW", "Mazda", "Audi", "Chevy", "Honda", "Ferrari", "Mclaren"]
randommodel = ["Vroom", "Acer", "Macan", "Macan S", "Boxster", "Panamera", "Corolla", "911", "Charger", "Supra", "F-150", "Miata", "R8", "Aventador", "G-Wagon"]
randomcolors = ["Blue", "Black", "White", "Red", "Pink", "Rainbow", "Yellow", "Green"]
topspeed = ["180", "200", "220", "240", "260", "500"]

iselectric = ["True", "False"]

class Car():
    def __init__(self, make, model, year, randomcolors, topspeed, iselectric, caremoji):
        self.make = make
        self.model = model
        self.year = year
        self.topspeed = topspeed
        self.iselectric = iselectric
        self.randomcolors = randomcolors
        self.caremoji = caremoji



    def showcarstats(self):
        clear_screen()
        time.sleep(0.2)
        print("Make: " + self.make)
        print("Model: " + self.model)
        print("Year: " + str(self.year))
        print("Top Speed: " + str(self.topspeed) + " km/h")
        print("Electric: " + str(self.iselectric))
        print("Color: " + self.randomcolors)

    def animatecars(car1, car2):
        pos1 = 0
        pos2 = 0

        for _ in range(30):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Car 1: " + " " * pos1 + f"{car1.caremoji}")
            print(f"Car 2: " + " " * pos2 + f"{car2.caremoji}")
            time.sleep(0.1)

            pos1 += int(car1.topspeed) // 50
            pos2 += int(car2.topspeed) // 50

            if pos1 >= 200 or pos2 >= 200:
                break

        if pos1 > pos2:
            print(f"{car1.make} {car1.model} wins! {car1.caremoji}")
        elif pos2 > pos1:
            print(f"{car2.make} {car2.model} wins! {car2.caremoji}")
        else:
            print("It's a tie!")





    def race(self, other):
        clear_screen()
        time.sleep(0.2)
        self.animatecars(car2)




def clear_screen():
    print("\n" * 100)





car1 = Car(
    random.choice(randommake),
    random.choice(randommake),
    random.randint(1999, 2025),
    random.choice(randomcolors),
    random.choice(topspeed),
    random.choice(iselectric),
    random.choice(caremoji))



car2 = Car(
    random.choice(randommake),
    random.choice(randommake),
    random.randint(1999, 2025),
    random.choice(randomcolors),
    random.choice(topspeed),
    random.choice(iselectric),
    random.choice(caremoji))


 # -------------------------------------------------------------------------------------------------------



while True:
    print("1 = Show Random Car Stats")
    print("2 = Race 2 Random Cars")
    userinput = input("What would you like to do? ")
    if userinput == "1":
        car1.showcarstats()
        break
    if userinput == "2":
        Car.race(self=car1, other=car2)
        break
    else:
        print("Not a valid choice.")




















