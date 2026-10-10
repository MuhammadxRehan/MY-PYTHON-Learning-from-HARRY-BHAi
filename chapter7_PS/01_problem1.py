#  Write a program to print multiplication table of a given number using for loop.
n =int(input("Enter a number: "))
# basically in this ii did that we wants to print 1to 10
# as we know start and stop indixing in python  stop means
# 'stop = n-1' soo it will print 1 to 10 ..

for i in range(1,11):
    print(f"{n} X {i} = {n*i}" )
# we used "f" function as to write variable in string