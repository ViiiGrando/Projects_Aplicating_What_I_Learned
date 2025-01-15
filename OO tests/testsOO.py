class Car:
    
    car_quantity = 0 # attribute class

    def __init__(self, color, model):#constructor method, always uses self as a reference parameter, and defines the object's attributes
        self._color = color# object's atributes
        self.model = model
        Car.add_car() #add one to the cars class attribute
        
    def __str__(self):
        return f'{self._color} | {self.model}' 


    def show_caracterists(self):#common class method, I can use it on unique objects in my class, 
                                 #each one with a different parameter according to the parameters assigned to the constructor method

        print("Car's caracterists:")
        print(f'Color: {self.color}')  #f 'strings for better {formatting}'  
        print(f'Model: {self.model}')
     
    @classmethod
    def add_car(cls):
        cls.car_quantity +=1  # modify the atribute car_quantity

    
    @classmethod
    def created_cars(cls):
        return f'Total cars created: {cls.car_quantity}'
    
    @classmethod
    def reset_counter(cls):
        cls.car_quantity = 0  # modify the atribute car_quantity

    @property#overall it improves readability, but I can use this method to return the value of an attribute
    def color(self):
      return self._color


#  class objects
car1 = Car("Blue", "Sportive")
car2 = Car("Red", "SUV")

# Call class method to get number of cars created
print(Car.created_cars())  # Output: total created cars

# Reset cars quantity
Car.reset_counter()

# show the new output of car's class attribute 
print(Car.created_cars())  # Output: Total created cars now is = 0