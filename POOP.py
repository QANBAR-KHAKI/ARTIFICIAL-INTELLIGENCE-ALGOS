class Car:
    def __init__(self, name, model, make):
        self.name = name    # these are the member variable
        self.make = make
        self.model = model


    def driving (self):
        print("This car is driving ")

    def stop (self):
        print("This car is stopped")
    
    def print(self):
        print(f"my car name is {self.name} and my model is {self.model}\n")
    
    
#main function

c=Car("Sonata",2023,"Hyundai")
print(c.driving(),c.make,c.name,c.stop())