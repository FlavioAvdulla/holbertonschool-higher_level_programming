class Dog:

    species = "pastor"

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def description(self):
        return (f"The {self.__name} is {self.__age} years old")

def main():
    my_dog = Dog("Buddy", 18)
    print(my_dog.description())

if __name__ == "__main__":
    main()
