# basically is a walrus operator which in used to assign a value to variable in expression
# syntax:  variable name  colon(:) with equal (=) and value 


if (n := len([23,2,43,121,]) > 3):
    print("Working")
else:
    print("Not working")