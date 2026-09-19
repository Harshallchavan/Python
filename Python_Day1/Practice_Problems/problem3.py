# Write a python program to print the contents of the directory using os module.

import os

file_path = r"C:\Users\harsh\Desktop\Python\Python\Python_Day1\Practice_Problems\example.txt"

if os.path.exists(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            print(content)

    except PermissionError:
        print("Permission denied: Cannot read this file.")

    except Exception as error:
        print("An error occurred:", error)
else:
    print("File not found.")