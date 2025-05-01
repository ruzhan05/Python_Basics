d = {} # empty dictionary

marks = {
    "Harry": 79,
    "Shubham": 60,
    "Rohan": 40,
    0: "Ruzhan",
    "list": [2,4,5]
}

# list values but associated with keys
# Here Harry, shubham and Rohan are the keys with different values and under the same "marks" dictionary

#different keys with their values are stored in the same collection

print(marks, type(marks))

print(marks["Harry"]) #prints value of the key
marks1 = [["Harry", 79],["Shubham", 60],["Rohan",40]]
# this can work. But for this it is hard to work with/find the indexes when it is a large program. That is why dictionaries are used.
print(marks["list"][0])