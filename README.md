# Car Sales Application

## Assignment:
This application is the final project for CIS 120

## Description:
This project is a car sales application. A menu-driven application to select any amount of options (at least 2 sets of options, e.g. vehicle type and engine type, each option must be priced differently) and calculate the total price of the vehicle. Written in python3.

## DESCRIPTION OF VARIABLES AND FUNCTIONS:

### Variables:
* **type** [*string*]: 
    - Description: The type of vehicle. 
    - Options: SUV, Sports, Compact. 
    - Default: "N/A" 
* **color** [*string*]: 
    - Description: The color of the car. 
    - Options: Green, Metallic Pink, 24k Gold
    - Default: "N/A"
* **interiorFabric** [*string*]: 
    - Description: The material the interior is made from. 
    - Options: Cloth, Leather
    - Default: "N/A"
* **typeCost** [*int*]: 
    - Description: The additional cost for the type var above
    - Default: 0
* **colorCost** [*int*]: 
    - Description: The additional cost for the color var above
    - Default: 0
* **interiorFabricCost** [*int*]: 
    - Description: The additional cost for the interiorFabric var above
    - Default: 0
* **basePrice** [*int*]: 
    - Description: The default price of the car. The total price for the car is basePrice+typeCost+colorCost+interiorFabricCost
        
### Functions:
* **choseType**:
    - *Description*: Prompts the user for a type option. The option is validated. The chosen type is stored at type and the associated cost is stored as typeCost.
    - *Parameters*: none
    - *Return*: void
* **chooseColor**:
    - *Description*: Prompts the user for a color option. The option is validated. The chosen color is stored at color and the associated cost is stored as colorCost.
    - *Parameters*: none
    - *Return*: void
* **chooseInteriorFabric**:
    - *Description*: Prompts the user for a interior fabric material. The option is validated. The chosen material is stored at interiorFabric and the associated cost is stored as interiorFabricCost.
    - *Parameters*: none
    - *Return*: void
* **calcPrice**:
    - *Description*: This function adds the basePrice and additional costs associated with the options selected.
    - *Parameters*: none
    - *Return*: [*int*] Dollar value of the total price of the car with all additional costs added.
* **saveResults**:
    - *Description*: This function writes the provided dictonary to a file as a string. It can later be parsed back into a python dictonary
    - *Parameters*: dictonary as dict
    - *Return*: void
    