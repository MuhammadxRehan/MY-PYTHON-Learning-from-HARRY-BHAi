# Create a class ‘Employee’ and add salary and increment properties to it. 

class Employee:
    
    salary = 234
    increment = 20
    # this "@property decorator" is used to directly print the value 
    @property
    def salaryafterincrement(self):
        return(self.salary + self.salary * (self.increment/100))
    
    @salaryafterincrement.setter
    def salaryafterincrement(self , salary):
        self.increment= ((salary/self.salary)-1)*100




em = Employee()
# print(em.salaryafterincrement)
em.salaryafterincrement = 300
print(em.increment)

