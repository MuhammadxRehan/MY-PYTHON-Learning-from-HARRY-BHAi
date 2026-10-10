f = open("rehan.txt")

content = f.read()
print("File Content:", repr(content))   # repr() se exact content show hoga

f.close()