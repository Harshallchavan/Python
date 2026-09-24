# functions used to manipulate the string or get the information about the string
# 1) len()

name="Harshal"
print(len(name))

#ends with 
print(name.endswith("Ha")) # gives true or false accordingly if the string ends with specified letters check the string
#starts with
print(name.startswith("Ha"))# check the string and give true or false value if the string starts with the provided values
#Capitalize string
print(name.capitalize())# only capatlize the start letter of the string 
#upper
print(name.upper())# capatlize  all values in the string
#lower 
print(name.lower())# samll all the values in the string
#title()
print(name.title())#capatlize the first character of each word 
#strip()
print(name.strip())# remove extra space from front of the string
#replace()
print(name.replace("Harshal","Radhika")) # replace the word in the string with 
#find()
print(name.find("s"))# position at index value
#count()
print(name.count("a")) # to count the number of letters or words in the string
#split()
print(name.split())# split the string into parts
#join()
# print(name.join())#converts list to string
#isalpha()
print(name.isalpha())#check where all words in strings are alphabets
#isdigit()
print(name.isdigit())# check whether all the char in string are digits(1234)
#isalnum
print(name.isalpha())#check the char is sring are alphabet + numbers

