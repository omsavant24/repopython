#1
"""print("hello world")"""
#2
"""name=input("enter your name:")
age=input("enter yor age:")
print("your name is",name,"and age is:",age)"""

#3 calculator
'''a=int(input("enter the number"))
b=int(input("enter the number"))
print("sum:",a+b)
print("sub:",a-b)
print("div:",a/b)
print("multiplication:",a*b)
print("reminder:",a%b)
'''
#4
'''celsius=float(input("enter the temp"))
fahrenheit=(celsius*9/5)+32
print(celsius,"is equal to",fahrenheit)'''
#5 swap
'''a=int(input("enter your number"))
b=int(input("enter ur 2nd number"))
print ("before swapping a =",a,"and b =",b)
a,b=b,a
print("after swapping a =",a,"after swapping b =",b)'''
#6 even odd
'''a=int(input("enter your number"))
if a%2==0:
    print("even")
else:
    print("old")'''
#7 vowel and consonent
'''a=input("enter letter")
if a in ('A','E','I','O','U','a','e','i','o','u'):
    print("your letter is vowel")
else:
    print("your letter is Consonant")'''

#8 square,cube,cube root
'''a=int(input("enter the number:"))
print("square:",a*a)
print("cube:",a*a*a)
print("sqaure root:",a**1/2)'''

#area of circle
'''redius=float(input("enter your radius:"))
area=3.14*(redius**2)
print("area of cricle is:",area)'''

#simple int calculator
'''princpal_amount=int(input("enter your principal value:"))
rate_of_int=float(input("enter uour rate of int:"))
time=float(input("enter your borrowing time in yr:"))

simple_int= (princpal_amount*rate_of_int*time)/100
print("simple intrest:",simple_int)'''

#Largest of Three Numbers
'''num1 =float(input("enter num 1:"))
num2 =float(input("enter num 2:"))
num3 =float(input("enter num 3:"))
if num1==num2==num3:
    print("all are equal")
else:
    largest_num=max(num1,num2,num3)
    print(largest_num)'''

#leap yr

#multiplication table
'''Table=int(input("enter number:"))
for i in range (1,11):
     print(Table, "*", i, "=", Table * i)'''

#sum of n natural num
'''n = int(input("Enter your number: "))
sum_no = sum(range(1, n+1))
print("The sum of numbers from 1 to", n, "is:", sum_no)
'''
#factorial
'''import math
n=int(input("enter you nmber"))
result=math.prod(range(1, n+1))
print(result)'''

#simple calulator by def function
'''def simple_calculator():
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    choice = int(input("Enter your choice (1/2/3/4): "))      
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    if choice == 1:
        print("Addition is:", num1 + num2)
    elif choice == 2:
        print("Subtraction is:", num1 - num2)
    elif choice == 3:
        print("Multiplication is:", num1 * num2)
    elif choice == 4:
      
        if num2 != 0:
            print("Division is:", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid choice! Please select a number between 1 and 4.")


simple_calculator()'''

#power function
#Count Characters in a String (Function)
'''def cnstring(your_string):
    return len(your_string)

    
print(cnstring("Happy Birthday King"))'''

#Check Prime (Function)
'''def is_prime():
    n=int(input("enter the number"))
    if n<=1:
        print("number is not prime")
    for i in range(2,n):
        if n%i==0:
            print("not prime")
        else:
            print("number is prime")

is_prime()'''

#fibonachi series
'''def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = [0, 1]
        for i in range(2, n):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
        return fib_list


print(fibonacci(10)) '''

#gcd
'''import math

def gmc(a, b):
  
    gcd_value = math.gcd(a, b)
    return gcd_value


print(gmc(56, 98))'''

#lcm
'''import math
def lcm(a,b):
    abs_val=abs(a)
    gcd_value = math.gcd(a, b)
    

    lowest_cm=abs_val/gcd_value
    return lowest_cm

print(lcm(56,98))'''

#tower_of_hanoi
def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n-1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n-1, auxiliary, destination, source)

tower_of_hanoi(3, 'A', 'C', 'B')  

    
    
    




















































         
        









    






#random num guess
'''import random

random_num = random.choice(range(1, 101))  # Randomly pick a number between 1 and 100
print("A number has been generated. You have 5 attempts to guess it.")

x = 0  
while x < 5:
    x += 1  
    choose = int(input(f"Attempt {x}: Enter your guessed number: "))
    if choose > random_num:
        print("Too high! Try again.")
    elif choose < random_num:
        print("Too low! Try again.")
    elif choose == random_num:
        print(f"Congratulations! You guessed it right in {x} attempts.")
        break  

if x == 5 and choose != random_num:
    print(f"Sorry, you've used all your attempts. The number was: {random_num}")'''


#count degits of num
'''num=int(input("enter the number"))

count=len(str(num))
print("count of number",count)'''
#reverse num
'''num = int(input("Enter a positive integer: ")) 
reversed_num = int(str(num)[::-1])  
print("Reversed number:", reversed_num) '''

#samwe in while

'''num=int(input("enter the number"))
result=0

while num!=0:
    degit=num%10
    result=result* 10 +degit
    num=num//10
print("Reversed number:", result)'''

#sum of od even sep

'''numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


even_sum = 0
odd_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")'''

#palidrom
'''num=int(input("enter the number"))
reversed_num = int(str(num)[::-1])
if num==reversed_num:
    print("palidrom")
else:
    print("normal number hai bhai")'''


    

    










    



