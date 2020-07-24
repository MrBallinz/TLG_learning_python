# Day five lab
# the two primary number types in python are integers and float points

# variables
x = 5
pi = 3.14
radius = 6
name = input("Enter in your first name: ")
surname = input("Enter in your last name: ")
question = input('Is this basic training difficult? ')
budget = int(input("How much bread you got for this bread?"))


print(pi * radius**2)
print(name + " " + surname)
print(name.lower() + " " + surname.upper())

if question == "yes":
    print("you a smooth criminal")
else:
    print("try your chances at the lottery")

#budget
if budget <= 0:
    print('error')
elif budget > 1000:
    print('error too much bread')
elif budget > 550:
    print('you will eat goooood this month')
elif budget == 550:
    print("You eatin with the rest of us big dawg")
elif budget < 550:
    print("get them side hustles in cause you gonna be hungry")

#even number counter

start, end = 0,100

# iterating each number in list
for num in range(start, end + 1):

    # checking condition
    if num % 2 == 0:
        print(num, end=" ")
# random number list
import random

nums  = []

for i in range(1,101):
    n = random.randint(1,100)
    nums.append(n)
print(nums)