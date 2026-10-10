class Empolyee:
    a= 10 

class programer(Empolyee):
   b = 11

class manager(programer):
    c= 12

o= Empolyee()
print(o.a)
o =programer()
print( o.a , o.b)
o = manager()
print(o.a  ,o.b, o.c)
