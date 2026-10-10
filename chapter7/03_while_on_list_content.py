#  Write a program to print the content of a list using while loops. 
# we have a list that value is differ from each other and list in list
h=["rehan", "ali","hami", "izan", 1,12.45,["hammad and rehan"]]
# the variable "i" is used to repeat the value to given condition times 
i=0
# the condition is that countinue to print if i less than lenght of list "h"
# otherwise loops will exhousted 
while(i<len(h)):
    # the output is list and big brakets show how much times  repeated
    print(h[i])
    # it show increament will one to next 
    i+=1