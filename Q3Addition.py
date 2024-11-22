# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.
import random
A = random.randint(1,100)
B = random.randint(1,100)
print(A,"+",B,"= ?")
while True:
    try:
        inp = int(input())
        if inp == A+B:
            print("You got it right")
            break
        else:
            print("You got it wrong, try again")
    except:
       1+1