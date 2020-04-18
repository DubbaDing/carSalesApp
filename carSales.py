class Car:
    # This class controls the Car object.
    # vars: type, color, interiorFabric, typeCost, colorCost, interiorFabricCost, basePrice
    # functions: chooseType, chooseColor, chooseInteriorFabric, calcPrice

    def __init__(self):
        # set defaults
        self.type = "N/A"
        self.color = "N/A"
        self.interiorFabric = "N/A"
        self.typeCost = 0
        self.colorCost = 0
        self.interiorFabricCost = 0
        self.basePrice = 1000

    # this function prompts and sets the type and additional cost of their car.
    def chooseType(self):
        typeChoice = 0
        
        # repeat until valid option
        while typeChoice < 1 or typeChoice > 3:
            print("\n\nWhat type of car would you like?\n")
            print("1.\tCompact\t+$0")
            print("2.\tSUV\t+$1000")
            print("3.\tSports\t+$3000\n")
            typeChoice = int(input("Choice: "))
        # Set the text and additional cost
        if typeChoice == 1:
            self.type = "Compact"
        elif typeChoice == 2:
            self.type = "SUV"
            self.typeCost = 1000
        elif typeChoice == 3:
            self.type = "Sport"
            self.typeCost = 3000

    def chooseColor(self):
        colorChoice = 0

        # this function prompts and sets the color and additional cost of their car.
        while colorChoice < 1 or colorChoice > 3:
            print("\n\nWhat color would you like?\n")
            print("1.\tGreen\t+$0")
            print("2.\tMetallic Pink\t+$100")
            print("3.\t24k Gold\t+$300\n")
            colorChoice = int(input("Choice: "))
        # Set the text and additional cost
        if colorChoice == 1:
            self.color = "Green"
        elif colorChoice == 2:
            self.color = "Metallic Pink"
            self.colorCost = 100
        elif colorChoice == 3:
            self.color = "24k Gold"
            self.colorCost = 300

    def chooseInteriorFabric(self):
        fabricChoice = 0

        # this function prompts and sets the interior fabric and additional cost of their car.
        while fabricChoice < 1 or fabricChoice > 2:
            print("\n\nWhat interior fabric would you like?\n")
            print("1.\tCloth\t+$0")
            print("2.\tLeather\t+$400\n")
            fabricChoice = int(input("Choice: "))
        # Set the text and additional cost
        if fabricChoice == 1:
            self.interiorFabric = "Cloth"
        elif fabricChoice == 2:
            self.interiorFabric = "Leather"
            self.interiorFabricCost = 400

    # calculates and returns the base price plus the add-on costs for the chosen options
    def calcPrice(self):
        return (int(self.basePrice) + int(self.colorCost) + int(self.interiorFabricCost) + int(self.typeCost))

currentCar = Car()
menuChoice = 0
print("\n\n#####################################")
print("##                                 ##")
print("##  Welcome to the car buying app  ##")
print("##                                 ##")
print("#####################################")

while True:
    
    print("\n-------------------")
    print("Please choose your options")
    print("Total: $", currentCar.calcPrice(), "\n")
    print("1. Car Type:", "\t\t", currentCar.type, "\t+ $",currentCar.typeCost)
    print("2. Color:", "\t\t", currentCar.color, "\t+ $", currentCar.colorCost)
    print("3. Interior Fabric:", "\t", currentCar.interiorFabric, "\t+ $", currentCar.interiorFabricCost)
    print("4. Finished!\n")

    menuChoice = int(input("What option would you like to change?: "))
    if menuChoice == 1:
        currentCar.chooseType()
    elif menuChoice == 2:
        currentCar.chooseColor()
    elif menuChoice == 3:
        currentCar.chooseInteriorFabric()
    elif menuChoice == 4:
        actuallyQuit = True
        quitChoice = None
        if currentCar.type == "N/A" or currentCar.color == "N/A" or currentCar.interiorFabric == "N/A":
            quitChoice = input("You didn't choose all options. Are you sure you want to quit? [y/n]: ")
            if quitChoice == "y":
                break
        else:
            break
    print("\n\n")


# display the price
print("Your", currentCar.color, currentCar.type, "with", currentCar.interiorFabric,"will set you back $", currentCar.calcPrice())
