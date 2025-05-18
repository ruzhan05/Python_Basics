# for loop to print 1 to 99

for i in range (1,100):
    print(i)

# for i in range (4) # for i in range (0,4)  (((SAME)))

# This code goes forward by 4 steps (prints 0,4,8,....)

for i in range (0,100, 4):
    print(i)
    

# iterating all the elements inside a list by using for loop

l = ["Harry", "Hello","Is","A","Very","Good", "Coder"]

for i in l:
    print(i)

# Can be used with Tuples as well

print("This is for Tuples")

t  =(122,222,444,"String", 3344)

for j in t:
    print(j)
    
# for loop can also be used to iterate through each words of the string

s = "Ruzhan"

for k in s:
    print(k) 
else:
    print("The name has been printed fully")  # This is printed when the for loop exhausts

# The above for loop prints:
# R
# u
# z
# h
# a
# n

# else condition can also used with for loop (Check above example)


## Break and continue with for loops

for i in range(100):
    if(i==34):
        break  #This will exit the whole loop
    print(i)
    
    

for i in range(100):
    if(i==34):
        continue    #This will skip the iteration. (Here it will skip printing the number 34)
    print(i)
    

# Pass in for loop

for i in range(645):
    pass             #pass keyword instructs pyhton that this block or for loop should not be considered now. It may be needed later. Without the "pass" keyword the code will show error, if there is no code statement inside the for loop.
i = 0    
while(i<45):
    print(i)