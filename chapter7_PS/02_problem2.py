# Write a program to greet all the person names stored in a list ‘l’ and which starts 
# with S. 
# this is a simple list..
l = ["Harry", "Soham", "Sachin", "Rahul"]
# we used "for loop" on list 'l' with variable "name" 
for name in l:
    # we do "if" condition as where in list first name start with 
    # capital S than print hello  with the name 
    if(name.startswith("S")):
        print(f"hello {name}") 
        # we used "f" function as to write variable in string
