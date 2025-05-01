# # 1
# words = { 
#    "madad": "Help",
#     "kursi": "Chair",
#     "billi": "Cat"
# }

# word = input("Enter the word you want to know the meaning of: ")

# print(f"The translated word is " , words[word]) # when you enter a key, it will return its value

# 2

# a = int(input("Enter the 1st number: "))
# b = int(input("Enter the 2nd number: "))
# c = int(input("Enter the 3rd number: "))
# d = int(input("Enter the 4th number: "))
# e = int(input("Enter the 5th number: "))
# f = int(input("Enter the 6th number: "))
# g = int(input("Enter the 7th number: "))
# h = int(input("Enter the 8th number: "))
# s = {a,b,c,d,e,f,g,h}
# print(type(s))
# print(s)


## alternative

# s = set()
# n = input("Enter the number : ")
# s.add(n)
# n = input("Enter the number : ")
# s.add(n)
# n = input("Enter the number : ")
# s.add(n)
# n = input("Enter the number : ")
# s.add(n)
# n = input("Enter the number : ")
# s.add(n)
# n = input("Enter the number : ")
# s.add(n)
# n = input("Enter the number : ")
# s.add(n)
# n = input("Enter the number : ")
# s.add(n)
# print(s)


# 3 yes

# 4
# s = set()
# s.add(20)
# s.add(20.0) # 1 == 1.0 is True, so it is considered as a duplicate. So it will not be included in the set

# s.add("20")
# print(len(s))

# 6
dict = {
    
}

name = input("Enter friends name: ")
lang = input("Enter the fav langauge: ")
dict.update({name:lang})
name = input("Enter friends name: ")
lang = input("Enter the fav langauge: ")
dict.update({name:lang})
name = input("Enter friends name: ")
lang = input("Enter the fav langauge: ")
dict.update({name:lang})
name = input("Enter friends name: ")
lang = input("Enter the fav langauge: ")
dict.update({name:lang})
print(dict)


# if we enter the same key 2 times with different values, it will show the key only one time and with the latest value, as we used update method here.

# the value can be duplicated, but the key cannot be duplicated

# "Harry": "C++", "Rohan": C++

# but if,
# "Harry": C++, "Harry": Js,    then the dict will hahve the value as "Harry": Js

# 9 

s ={8, 7,12,"Harry", [1,2]}

# the list inside a set cannot be modified

# Infact, list cannot be included in a set, because set is immutable and list is not