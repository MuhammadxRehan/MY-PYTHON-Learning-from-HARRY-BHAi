# # while loops:
# '''
# while is type of loop in which , this used to a task for many times execute
# untill a condition met False... if condition True it will works otherwise 
# it will not execute more .... it will not work on False condition 
# each times while axecuting it check the condition..
# '''
# # simple loop
# h = 1
# while(h<20):
#     print(h)
#     h +=1

# '''
# sometimes wrong logic create the infinite loop which is unlimited while 
# executing ... so avoid from creating infinite loop.
# its creation is simple as write a condition that never False ....
# '''
# # infinite loop 
# """ the below loop is infinite as the condition is always True 
# due the variable 'h' is not concern in 'while' loop condition ....
# the condition in 'while' loop is not met soo it is an infinite loop
# if we put a condition  that will bacome the false condition in 'while' condition 
# then the loop will break down automaticlly  """

# h=0
# while (1<2):
#     print(h)
#     h +=1

# # this is also be a while loop
# ''' in below program  first we need a input that user will put down 
# the condition is that if the number will  5 then condition will false 
# and loop will exit and if the condition will not met then loop become a
# infinite loop .
# last line i don't understant yet.....?'''

# num=int(input("Enter a number: "))
# while num !=5:
#     print(num,num*num)
#     num = int(input("Enter a number"))

# this the a finte looop
''' we have variable count and condition will bacame false as count increase the value from 10 
and condition will finished and loop will exit 
count increase their value one by one as last line otherwise is finite loop will be created 

'''
# count=0
# while count<10:
#     print(count, count*count, count*count*count)
#     count +=1

# in this program
''' we used induxing for printing the value .... it print the value as lenght of list will 
be completed for condition and given indux will print one by one as last line 
'''

s= "karor"
lst=["rehan","hami", 34]
tpl= ("rehan", 45,-1,"ali")
i = 0
while i<len(lst):
    print(i,s[i],lst[i],tpl[i])
    i+=1