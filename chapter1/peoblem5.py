import os 
# which content we wants to list?
directory_path ='/'
# using os to list the directory 
content = os.listdir(directory_path) 
# print the content of directory of the list
for item in content:
    print(item)