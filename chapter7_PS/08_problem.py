#  8 Write a program to print the following star pattern. 
# * 
# ** 
# ***  for n = 3


n=int(input("Enter a number: "))
# in this range we do simple n+1 for in "n"
for i in range(1 , n+1):
#in that program just print i times 
    print("*" *(i),end ="" )
    # this last print function for just print deafult line  not extra new line
    print("")
