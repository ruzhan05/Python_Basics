def goodDay(name, ending):
    print("Good Day, " + name)
    print(ending)
    return "done"
    
a = goodDay("Ruzhan", "Thank you") # a will not get the value if the value is not returned by the function
print (a)

'''
 Good Day, Ruzhan       # printed by the function
 Thank you              # printed by the function
 
 done                   # returned by the function
'''


