class Car:
    def __init__(self, brand, car_name, year):
        self.brand = brand
        self.car_name = car_name
        self.year = year

    def display(self):
        print("Brand:", self.brand)
        print("Car Name:", self.car_name)
        print("Year:", self.year)
brand = input("Enter the brand of the car: ")
car_name = input("Enter the name of the car: ")
year = int(input("Enter the year of the car: "))
car1 = Car(brand, car_name, year)
car1.display()