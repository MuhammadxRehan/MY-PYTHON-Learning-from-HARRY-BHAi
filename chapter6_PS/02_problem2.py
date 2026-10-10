mark1 = int(input("Enter your narks1:"))
mark2 = int(input("Enter your narks2:"))
mark3 = int(input("Enter your narks3:"))

# if(mark1<=100 and mark1>=0 and mark2<= 100 and mark2>=0 and mark3<=100 and mark3>=0):
if(mark1<=100 and mark1>=0 and mark2<= 100 and mark2>=0 and mark3<=100 and mark3>=0):

    total_percentage =(100*(mark1+mark2 +mark3))/300
    if(total_percentage>=40 and total_percentage<=100 and mark1>=33 and mark2>=33 and mark3>=33):
        print("passed , percentage:",total_percentage)
    else:
        print("failed , percentage",total_percentage)
else:
    print("invalid input")