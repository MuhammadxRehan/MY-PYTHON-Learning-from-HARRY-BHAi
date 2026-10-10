from  random import randint
class train ():
    def __init__(self , trainNo ):
        self.trainNo = trainNo 
        

    def book(self, fromm, to ):
        print(f"Tickets booked in train no: {self.trainNo} from {fromm } to  {to }")


    def getstatus(self,   ):
        print(f"The train no :{self.trainNo} is running on time ")


    def getfare(self, fromm , to ):
        print(f"Tickets fare in train no: {self.trainNo} from {fromm } to  {to } is {randint(334,6660)}")


t = train (5679)
t.book("lahore", "Karachi")
t.getstatus()
t.getfare("lahore", "Karachi")