class Employeee:
    company = "ITC"
    def show(self):
        print(f"The is {self.name} and salary is {self.salary}")

# class programmer:
#     company = "ITC infotech "
#     def show (self):
#         print(f"The is {self.name} and salary is {self.salary}")
    
#     def showlangugae(self):
#         print(f"The is {self.name} and language is {self.language }")

class programmer(Employeee):
    company = "ITC infotech "
    def showlangugae(self):
         print(f"The is {self.name} and language is {self.language }")
 
a= Employeee()
b = programmer()
print(a.company , b.company )