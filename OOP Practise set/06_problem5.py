# 1. Create a class (2-D vector) and use it to create another class representing a 3-D 
# vector. 
# This is 2D vector class 
class TwoD_vectors:

    # 2D class instructor
    def __init__(self , i,j):
        self.i = i
        self.j = j
    #2D ouput function 
    def show(self):
        print(f"The 2D vector is: {self.i}i + {self.j}j")

# This is 3D vector class
class ThreeD_vectors(TwoD_vectors):
    # 3D class instructor 
    def __init__(self , i,j,k):
        super().__init__(i,j)
        self.k = k

    # 3D ouput function 
    def show(self):
        print(f"The 3D vector is: {self.i}i + {self.j}j + {self.k}k")

# These are objects 

a = TwoD_vectors(1,2)
a.show()
b = ThreeD_vectors(1,2,3)
b.show()
