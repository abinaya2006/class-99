import os 
import shutil

path=input("Enter the path of the folder that you want to sort: ")
list_of_files=os.listdir(path)

for file in list_of_files:
    name,ext=os.path.splitext(file)

    ext=ext[1:]
    if(ext==""):
        continue

    if os.path.exists(path + "/" + ext):
        shutil.move(path + "/" + file,path + "/" + ext + "/" + file)

    else :
        os.makedirs(path + "/" + ext)
        shutil.move(path + "/" + file,path + "/" + ext + "/" + file)

print("Your folder is sorted .")
