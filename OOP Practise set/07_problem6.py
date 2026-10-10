# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from 
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’. 
# This is empty class
class Animals:
    pass 

# This class from Animal class
class Pets(Animals):
    pass

# This class from Pets class
class Dog(Pets):
    @staticmethod

    def bark():
        print("Bow Bow!")

d = Dog(Pets)
d.bark()
        


        
