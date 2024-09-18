class Car:

    brand = "Toyota"

    def __init__(self, name, transmition, tires, color, production):
        self.__name = name
        self.__transmition = transmition
        self.__tires = tires
        self.__color = color
        self.__production = production
    
    def car_description(self):
        return(f"{self.__name} is very good car. It have {self.__transmition} transmition and {self.__tires} tires. The {self.__name} color is {self.__color} and year is {self.__production}.")

def main():
    car = Car("Corolla", "manual", "winter", "white", 2009)
    print(car.car_description())
    print()

if __name__ == "__main__":
    main()