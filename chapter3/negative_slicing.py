name = "Ruzhan"

print(name[0:3]) #slice the string

print(name[-4 : -1]) #slice the string from the end (negative index)
print(name[1:4]) #slice the string (corresponding to the negative index)
print(name[-4:]) #slice the string (incase of negative slicing, to get the last index, we don't need to specify the last index)

print(name[:4]) #slice the string from the beginning (if no number at the beginning, it starts from index 0)
print(name[1:]) #slice the string from the given index to the last index


# Slicing with skip value

a = "123456789"
print("The sliced number is", a[1:7]) #slicing without skip value
print(a[1:7:2]) #slicing with skip value of 2