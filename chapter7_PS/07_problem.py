#  7. Write a program to print the following star pattern. 
#   * 
#  *** 
# *****  for n = 3


n=int(input("Enter a number: "))
# in this range we do simple n+1 for in "n"
for i in range(1 , n+1):
    # n-i show that our space will less than variable in for loop 
    print(" "*(n-i) ,end ="" )
#in that print  funtion we do that starts will a number series 
    print("*"*(2*i-1),end ="" )
    # this last print function for just print new  not extra new line
    print("")
