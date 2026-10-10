a = open("rehan.txt")
content = a.read()
if("rehan" in content ):
    print("the word rehan is in content")
else:
    print("The word rehan is in content")
a.close()
