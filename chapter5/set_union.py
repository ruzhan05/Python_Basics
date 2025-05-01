s1 = {1,45,6}
s2 = {7,8,1,78}

print(s1.union(s2)) # this one returns in ascending order

print(s1.intersection(s2))

s1.update(s2) # copies all the elements of s2 to s1 and updates s1
print(s1)

print(s1.difference(s2)) # excludes the common elements between s1 and s2 from s1

