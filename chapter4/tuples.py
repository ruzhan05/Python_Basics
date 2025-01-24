# immutable data type in python (similar to lists but not immutable)
# cannot be changed like strings

a = (1,2,5,7,9) # first bracket with more than 1 data indicates tuple

a = (1) # this one will be considered as int

# need to put a comma to indicate that it is a tuple
a = (1,) # this one will be considered as a tuple


# a[0] = 34 # cannot be changed

b = (1,2, "ruzhan", False, "tamz")

print(type(a))

# Methods used in tuples

no = b.count("tamz")
print(no) 

i = b.index(False)
print (i) #returns the index number of the element

# multiply or repeat the elements in a tuple

tuple1 = (1,2,3)
repeatTuple = tuple1*4 # the same tuple will be repeated 4 times
print(repeatTuple)

# "in" keyword

tuple2 = ("ruzhan", 2, "aiman", 4)
print("aiman" in tuple2) # will return True is the element exists in the tuple (can be used to find if a specific element exists in a tuple)

# max and min value of a tuple

print (min(a)) # returns the minimum value

# "len" method to know the length of the tuple

# slicing 

newTuple = tuple2[1:3] # prints the element in the index 1 and 2
print(newTuple)

# unpacking

a,b,c,d = tuple2
print(a,b,c,d) # breaks the tuple and prints the element outside of the tuple

