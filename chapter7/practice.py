# # 1

# n = int(input("Enter the number : "))
# i = int(input("Enter the number of multiples you want to have : "))

# for multiplier in range (1, i+1):
#     print(f"{multiplier} X {n} = {multiplier*n}")
    
    
# # 2
# l = ["Harry","Sadman","Shakib","Sabbir","Tamim"]

# for j in l:
#     if(j[0]=="S"):
#         print(f"Greetings Mr. {j}")
#     else:
#         print(f"No greetings for you Mr. {j}")
    
#        #      OR   
    
# for j in l:
#     if(j.startswith("S")):
#         print(f"Greetings Mr. {j}")
#     else:
#         print(f"No greetings for you Mr. {j}")
    
# 3

# m = int(input("Enter the number you want to multiply: "))
# multi = int(input("Enter the number of times you want to multiply: "))
# k=0

# while(k<=multi):
#     print(f"The multiplication of {m} and {k} is: {m*k}")
#     k+=1
    
    
# 4

# n = int(input("Enter the number: "))

# for i in range(2,n):
#     if(n%i==0):
#         print("The number is not prime")
#         break
# else:
#     print("Number is prime")
    
# 5
# n = int(input("Enter the number: "))

# i = 1
# sum = 0
# while(i<=n):
#     sum = sum +i
#     i = i+1 
# print(sum)


# 6
# n = int(input("Enter the number"))

# product = 1
# for i in range (1,n+1):
#     product = product *  i
# print (f"The factorial of {n} is {product}")  

# 7

#           Star pattern problems

'''
n =3
  *
 ***
***** 
'''

# n = int(input("Enter the number: "))
# for i in range (1,n+1):
#     print(" " * (n-i), end="" )
#     print("*" * (2*i-1), end="")    # If we use the end = "", the print statement does not add a new line by default
#     print("")
    
    
# 8

# n = int(input("Enter the number: "))

# for i in range(1,n+1):
#     print("*" *i )
    
    
# 9

'''
* * *
*   *
* * *
'''


n = int(input("Enter the number: "))
for i in range (1,n+1) :
  if(i==1 or i == n):
    print("*" * n,end="")
  else:
    print(f"*", end="")
    print(f" "* (n-2), end="")   # because there has to be 2 stars, one at the start and one at the last. The rest has to be filled with spaces
    print(f"*", end="")
  print("")












# 10 

# n = int(input("Enter the number : "))
# i = int(input("Enter the number of multiples you want to have : "))
# for multiplier in range (1, i+1):
#     print(f"{i+1-multiplier} X {n} = {(i+1-multiplier)*n}")
