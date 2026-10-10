class imployee:
    name= input("Enter your name: ")
    language = "python"
    pay = 450000
    def getinfo(self):
        print(f"The language is {self.language}.The salaey is {self.pay}.")
    def salam(self):
        print(f"Assalam o Alikum {self.name}")
re = imployee()
re.language ="javascript"
# re.name = "rehan"
print(re.name , re.pay,re.language)
re.getinfo()
re.salam()