# Create a program that accepts 2 numbers from the user. 
# Your program will output a random number between the range given by the user.
import random
A = int (input("please enter a number: "))
B = int (input("please enter a number: "))
print(random.randint(min(A,B),max(A,B)))