class Automobile:

    NO_OF_GEARS = 6   # static constant

    def __init__(self):
        self.__color = None
        self.__speed = 0
        self.__make = None

    # Getter and Setter for color
    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    # Getter and Setter for speed
    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

    # Getter and Setter for make
    def get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make

    # Brake method
    def brake(self):
        if self.__speed == 0:
            print("Car already stopped")
        else:
            self.__speed -= 10
            print("Current speed:", self.__speed)

    # Accelerator method
    def accelerator(self):
        if self.__speed >= 400:
            print("Speed limit is high, please apply brake")
        else:
            self.__speed += 10
            print("Current speed:", self.__speed)

    # Change Gear method
    def change_gear(self, gear):
        if gear > Automobile.NO_OF_GEARS:
            print("Invalid gear...")
        elif gear == 1:
            print("Gear switched to 1")
            self.__speed = 20
            print("Current speed is:", self.__speed)


car = Automobile()
car.set_color("Red")
car.set_make("BMW")

car.accelerator()
car.accelerator()
car.brake()
car.change_gear(1)
