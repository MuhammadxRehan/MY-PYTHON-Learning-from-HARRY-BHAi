class imployee:
    language = "python"
    pay = 450000

    def __init__(self , name , language , pay):
        self.name = name 
        self.language= language
        self.pay = pay 

        print("I am creating an object: ") 

    # def getinfo(self):
    #     print(f"The language is {self.language}.The salaey is {self.pay}.")

    @staticmethod
    def salam(self):
        print(f"Assalam o Alikum")

re = imployee("rehan", "python",500000 )
print(re.name ,re.pay,re.language,)
# re.getinfo()
