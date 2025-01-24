# Q1


list1 = []
num = int(input("How many fruits do you want to add? "))
for i in range (num) :
    a = input(f"Enter the number {i+1} fruit ")
    list1.append(a)
    
print(f"The list of the fruits are : {list1}")


# Q2

list2 = []

num2 = int(input("How many students' marks do you want to enter? "))

for i in range (num2):
    marks = int(input(f"The marks of student {i+1} is: "))
    list2.append(marks)
print(list2)
# print(f"The marks of the student after sorting: {list2.sort()}") # The list is sorted, but cannot be displayed like this
list2.sort() # first need to sort, then need to print it again after sorting. Otherwise the sorted list cannot be printed
print(f"Sorted marks {list2}")


# bonus
num2 = (5,6,8)  # Tuple with one element
for i in num2:
    print(i)  # prints the elements in the tuple


# Q4
list3 = []
num3 = int(input("Enter the amount of numbers you want to enter in the list"))

for i in range (num3):
    c = int(input(f"Enter the {i+1} number: "))
    v = list3.append(c)
sum = 0
for j in list3: # j represents the elements in the list
    sum += j  # Add each element directly to the sum

print(f"The sum of the numbers in the list is {sum}")




# easy method

list4  = [10, 10,10]
print(sum(list4)) # returns 30


# Q5

b = (1,2,3,1,2,5,1)
n = b.count(1)
print(n)