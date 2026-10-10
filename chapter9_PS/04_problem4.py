word = "rehan"
with open("file.txt","r") as f:
    content=f.read()
contentnew= content.replace(word,"hammad" )
with open("file.txt","w") as f:
    f.write(contentnew)