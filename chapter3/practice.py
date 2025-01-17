#Q1

name = input("Enter your name: ")
print("Good morning" , name)

#new in python 3.6 or later

# f string
print(f"Good morning {name}")

#Q2

naam = input("Enter the name: ")
date = input("Enter the date: ")
print(f"""Dear {naam},
You are selected!
{date}""")


letter = """Dear <|Name|>,
You are selected!
<|Date|>"""

print(letter 
      .replace("<|Name|>", "Ruzhan").replace("<|Date|>", "24/01/2025")) 
#here first the string "<|Name|>" is converted to "Ruzhan" and then in the next step the date is replaced and the string is modified for the second time



#Q3

#Find the index where there is double space
# Returns -1 if there is no double space
#If anything, it returns a positive index number
str = "Harry is a good  boy"
print(str.find("  "))




# Q4
#Replace double space with single space

str = "Harry is a good  boy"
print(str.replace("  ", " "))
# here the str string does not change, rather a new string is created and printed

# replace function does not change the old string, it creates a new string from the old one Because strings ar immutable, you cannot change a string using any function


# Q5

lekha = "Dear Harry,\n\tThis pyhton course is nice.\n\tThanks!"
print(lekha)
