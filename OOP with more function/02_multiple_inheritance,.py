class Employeee:
    company = "ITC"
    name = "{default name}"
    def show(self):
        print(f"The is {self.name} and company is {self.company }")

class coder:
    language = "python"
    def printlanguages(self):
        print(f"Out of all the languages your language is: {self.language}")

class programmer(Employeee , coder):
    company = "ITC infotech "
    def showlanguages(self):
         print(f"The is {self.company} and language is {self.language }")
 
a= Employeee()
b = programmer()
b.show()
b.printlanguages()
b.showlanguages()