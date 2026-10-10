name = ("rehan ")
print(name[0:5]) #simple methods of string slicing 
print (name [:5]) # it is also same as firt method 
print(name [0:]) # it means that start to end encluding 
print(name [-4:-1]) # it means that nagative slicing with same result 
print(name [1:4]) # this  trick  not work to solve negative slicing 

 # skip slincing string
name = ("asdfghjkl")
print(name[1:4:2])
print(name[1:4])

#slicing with skip vaules 
a = ("jahggfkdjahgfkajsasjgfha")
print(a[0:5]) # this start to 4 (excluding 5)
print(a[0:5:4]) # answer of first colons :next colon 