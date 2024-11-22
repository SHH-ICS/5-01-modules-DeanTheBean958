# Create a program that will accept the two legs of a right-angle triangle, a and b, and display the length of the hypotenuse, c. 
# Remember to use prompts for the input and labels for the output. Use the formula a2 + b2 = c2 to calculate your answer.
import math
A = float (input("please enter the length of side A: "))
B = float (input("please enter the length of side B: "))
Csqaured = A ** 2 + B ** 2
C = math.sqrt(Csqaured)
print("For a right triangle wigth A = ", A,"And B = ", B,",the hypotenuse C =", C)