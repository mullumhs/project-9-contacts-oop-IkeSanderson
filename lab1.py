"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 1
---------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create and manipulate Car objects in Python to understand 
  basic concepts of Object-Oriented Programming.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
        self.is_engine_on = False
        self.odometer = 0

    def start_engine(self):
        self.is_engine_on = True
        print(f"The engine of the {self.color} {self.brand} is now on.")

    def stop_engine(self):
        self.is_engine_on = False
        print(f"The engine of the {self.color} {self.brand} is now off.")
    
    def drive(self,distance):
        if self.is_engine_on:
            self.odometer += distance
            print("Skrrt Skrrrrt")
        else:
            print("Engine is not on")


# Add another property to the Car class called "odometer".
# This property should be initialised to 0.



# Create two Car objects. One should be a red Toyota and the other a blue Ford.
Car1 = Car("Red","Toyota")
Car2 = Car("Blue","Ford")

# Start the engine of the red Toyota.
Car1.start_engine()


# Create a method called "drive" that takes a distance as a parameter.
# The car can only be driven if the engine is on.



# Attempt to drive both cars 100Km.
Car1.drive(100)
Car2.drive(100)

# Print the brand, odometer and colour of both cars.
print(f"Car 1 is a {Car1.color} {Car1.brand} that has driven {Car1.odometer}km")
print(f"Car 2 is a {Car2.color} {Car2.brand} that has driven {Car2.odometer}km")
