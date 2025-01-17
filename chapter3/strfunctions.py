name = "Ruzhan"

print(len(name)) #length of the string

print(name.endswith("an"))
print(name.startswith("Ruz"))
print(name.startswith("r")) #it is case sensitive
print(name.capitalize()) #capitalize the first letter of the string

word = "hello ruzhan aiman"
print(word.title()) #capitalize the first letter of each word in the string
print(word.replace("ruzhan", "aiman"))
print (word.upper())
print(word.split(" ", 1)) # 1 is the maxsplit, it means that the string will be splitted once based on the space. So only "hello" is split