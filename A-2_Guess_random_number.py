"""
Assignment 2: Guess random number
Write a Python program that will implement the following guessing game.
• Accept input from the user and check against a generated random number between 1 and 10. 
• If the input matches the random number, print “YOUR GUESS IS CORRECT” and exit. 
• If not, print “YOUR GUESS IS WRONG” and repeat the above process. 
• If the input is “exit”, then exit the loop. 
• If the input is not a number, print “YOU ENTERED AN INVALID NUMBER” and repeat the above 
process.
"""
import random

while True:
    num = input("Enter the number between 1 to 10: ")
    guess_num = random.randint(1,10)
    if num == 'exit':
        break
    elif not (num.isdigit()):
        print("YOU ENTERED AN INVALID NUMBER")
    elif int(num) == guess_num:
        print("YOUR GUESS IS CORRECT")
    elif int(num) != guess_num:
        print("YOUR GUESS IS WRONG")