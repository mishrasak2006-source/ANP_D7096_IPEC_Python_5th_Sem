'''---------- Number Guessing Game ------------------
A secret number is 37.

Keep asking the user to guess the number until
the correct number is entered.

Display whether the entered number is
too high, too low, or correct.
-----------------------------------------------------
Sample Output
Enter Guess : 20
Too Low
Enter Guess : 45
Too High
Enter Guess : 37
Correct Guess
-----------------------------------------------------'''
#-----------------------------------------------------
#---------------- Coding -----------------------------

secret = 37

for i in range(1, 6):

    guess = int(input("Guess the Number : "))

    if(guess == secret):
        print("Correct Guess")
        break
    elif(guess > secret):
        print("Too High")
    else:
        print("Too Low")
#-----------------------------------------------------

''' Output :
Enter Guess : 20
Too Low
Enter Guess : 45
Too High
Enter Guess : 37
Correct Guess
'''