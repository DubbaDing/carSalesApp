##############################
##  Car Buying Application  ##
##############################
#
#   Author      : Carl Caldwell
#   Date        : 04/17/2020
#   Assignment  : Final Project
#   Description : This is a menu driven program that helps select options and add additional costs for buying a car.
#   Filename    : carSales.py
#

class Car:
    # This class controls the Car object. Options available to the user are type, color, and interior fabric. Some options have additional costs associated with them.

    def __init__(self):
        # set defaults
        self.type = "N/A"
        self.color = "N/A"
        self.interiorFabric = "N/A"
        self.typeCost = 0
        self.colorCost = 0
        self.interiorFabricCost = 0
        self.basePrice = 7000

    # this function prompts the user and sets the type and sets the additional cost. Void return.
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
        # this function prompts the user and sets the color and sets the additional cost. Void return.
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
        # this function prompts the user and sets the interior fabric material and sets the additional cost. Void return.

        fabricChoice = 0
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

    def calcPrice(self):
        # calculates and returns the base price plus the add-on costs for the chosen options
        return (int(self.basePrice) + int(self.colorCost) + int(self.interiorFabricCost) + int(self.typeCost))

def saveResults(dict):
    # This function accepts a dictonary and writes it to a file. This function can later be adapted to save to a database
    file_append = open("completed.txt", "a")
    file_append.write(str(dict))
    file_append.close()

# create a new instance for a car
currentCar = Car()
menuChoice = 0 # used to store the user's current choice for the main menu

# print the main menu
print("\n\n#####################################")
print("##                                 ##")
print("##  Welcome to the car buying app  ##")
print("##                                 ##")
print("#####################################")

# run the main menu until we break from it with the "break" keyword
while True:
    # get/set the user the options
    print("\n-------------------")
    print("Please choose your options")
    print("Total: $", currentCar.calcPrice(), "\n")
    print("1. Car Type:", "\t\t", currentCar.type, "\t+ $",currentCar.typeCost)
    print("2. Color:", "\t\t", currentCar.color, "\t+ $", currentCar.colorCost)
    print("3. Interior Fabric:", "\t", currentCar.interiorFabric, "\t+ $", currentCar.interiorFabricCost)
    print("4. Finished!\n")
    menuChoice = int(input("What option would you like to change?: "))

    # parse the option
    if menuChoice == 1:
        # user wants to set the car type
        currentCar.chooseType()
    elif menuChoice == 2:
        # user wants to set the car color
        currentCar.chooseColor()
    elif menuChoice == 3:
        # user wants to set the interior fabric material
        currentCar.chooseInteriorFabric()
    elif menuChoice == 4:

        # user wants to finish
        # we should check to make sure they set all the options. It the user did not set an option, it will be equal to "N/A"
        if currentCar.type == "N/A" or currentCar.color == "N/A" or currentCar.interiorFabric == "N/A":
            # an option has not been set. Ask the user if they are sure they want to quit
            quitChoice = input("You didn't choose all options. Are you sure you want to quit? [y/n]: ")
            if quitChoice == "y":
                # the user has not finished selecting options, but wants to quit. End the app and don't add additional costs.
                break
        else:
            # the user wants to exit and has made a choice for each option
            break
    print("\n\n")


# Everything is done. Calc and display the final cost and a description to the user
print("Your", currentCar.color, currentCar.type, "with", currentCar.interiorFabric,"will set you back $", currentCar.calcPrice())

# Create an array and print to a file for storage (normally would use database)
carOptions = {
    "color": currentCar.color,
    "interiorFabric": currentCar.interiorFabric,
    "type": currentCar.type,
    "costs": {
        "color": currentCar.colorCost,
        "type": currentCar.typeCost,
        "interiorFabric": currentCar.interiorFabricCost
    }
}

saveResults(carOptions)


