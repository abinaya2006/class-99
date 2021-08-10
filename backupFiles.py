import os
import shutil

source=input("Enter the source of the folder: ")
destination=input("Enter the destination folder: ")

source=source + "/"
destination=destination + "/"

list_of_files=os.listdir(source)

for file in list_of_files:
    shutil.copy((source + file) , destination)

print("Backup is completed .")