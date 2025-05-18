# # 1
# def greatest(a,b,c):
#     if(a>b and a>c):
#         return(f"{a} is the greatest number")
#     elif(b>a and b>c):    
#         return(f"{b} is the greatest number")
#     else:
#        return(f"{c} is the greatest number")

# one = int(input("Enter the first  number: "))
# two = int(input("Enter the Second  number: "))
# three = int(input("Enter the third  number: "))

# print(greatest(one, two, three))

# # 2

# def f_to_c(f):
#     return 5*(f-32)/9

# f = int(input("Enter the temperature in Fahrenheit: "))
# print(f"{f_to_c(f)} degree Celsius")
        
# # 3

# print("a") 
# print("b") # prints b in the next line
# print("c",end = "") 
# print("d",end = "") # prints d in the same line as d without any spaces     

# 4


'''
sum(1) = 1
sum(2) = 1+2
sum(4) = 1+2+3+4

sum(n) = 1+2+3+....+ n-1 + n 
sum(n) = sum(n-1) + n
'''
# def sum(n):
#     if(n==1):
#         return 1
#     else:
#         return sum(n-1) + n
# m = int(input("Enter the number: "))
# print(f"The sum is {sum(m)}")


# 5 

'''
***
**
*
'''

# def pattern(n):
#     if(n ==0):
#         return
#     print ("*" * n)
#     pattern(n-1)

            
            
# pattern(5)

# 7

# def remove(l , word):
#     n = []
#     for item in l:
#        if not(item == word): 
#             n.append(item.strip(word)) # the strip methods removes the word or letter from the start and ending of a word
#     return n
# l = ["Harry", "Rohan", "Ruzhan", "an"]  
# print(remove(l, "an"))   # Harry is not removed because it does not have an at the begining or end


# 8

def multiply(n):
    for i in range (1,n+1):
        print(f"{i} x {n} = {i*n}")
multiply(11)
    