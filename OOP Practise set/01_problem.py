class programmer():
    company = "microsoft"
    def __init__(self , name ,pin , language ):
        self.name  = name 
        self.pin = pin 
        self.language= language 
p = programmer("rehan " , 78008, "python")
print(p.name , p.pin , p.language )