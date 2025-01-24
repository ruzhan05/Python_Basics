friends = ["akash", "ruzhan", 789,5.6, False]
friends[0] = "tamzid"
print(friends)
print(friends[1:3])

#Unlike strings lists are mutable
#List is similar to an array


# methods of List

# append (add an element at the end)
friends.append("Aiman")
print(friends)

#sort 

l1 = [1,34,62,2,6,11]
print(l1)
# l1.sort() #sort in ascending order for numbers
# print(l1)

# when I use sort on l1, then the l1 array becomes sorted. and the value of l1 becomes [1, 2, 6, 11, 34, 62]

# reverse
 

l1.reverse() # reverses the current order of the list (last index becomes 1st index)
print(l1)

# insert (insert in any particular index)
l1.insert(3, 444 ) # insert 333 into index 3

print(l1)

# pop (will delete element from a particular index and return it)

l1.pop(3) # pops out (takes out the element of the 3rd index from the list ) #printing this will return the element of the 3rd index
print(l1)

# remove

l1.remove(34) # removes a certain element with the value indicated here. In this case removes the element with value 34 from the list
print(l1)