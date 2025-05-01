marks = {
    "Harry": 79,
    "Shubham": 60,
    "Rohan": 40,
    0: "Ruzhan",
    "list": [2,4,5]
}
# print(marks.items())
# print(marks.values())
# print(marks.keys())
# marks.update({"Harry": 78, "New": 99}) #mutable
# print(marks)
# print(marks.get("Harry"))

# print(marks.get("unknown")) # gives "None" as output.   --This one better--
# print(marks["unknown"]) # returns error.

# pop method
# pop item
marks.popitem() # eliminates the last key/element in the dictionary
marks.pop("list") # takes an argument about which element is to be eliminated from the dictionary 
print(marks)

len(marks)