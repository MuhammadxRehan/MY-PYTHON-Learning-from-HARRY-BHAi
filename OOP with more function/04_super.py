class Empolyee:
    def __init__(self):
        print("The constructor of Employeee.")
    a= 10 

class programer(Empolyee):
    def __init__(self):
        print("The constructor of programmer.")
    b = 11

class manager(programer):
    def __init__(self):
        super().__init__()
        print("The constructor of manager.")
    c= 12

# o= Empolyee()
# print(o.a)
# o =programer()
# print( o.a , o.b)
o = manager()
print(o.a  ,o.b, o.c)