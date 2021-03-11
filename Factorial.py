# Factorial of a number using recursion

def fact(n):
   if n == 1:
       return n
   else:
       return n*fact(n-1)   #Recursion happening in this step

num = int(input("Enter Number: "))
print(fact(num))
