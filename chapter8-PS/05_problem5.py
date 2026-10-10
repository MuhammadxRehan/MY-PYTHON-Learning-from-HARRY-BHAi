def pattern(n,end=""):
    if(n==0):
        return 
    print("*"*n )
    pattern(n-1)
    
n =int(input("Enter a number: "))
print(pattern(n,end=""))
# discuss print none why
# ????1
