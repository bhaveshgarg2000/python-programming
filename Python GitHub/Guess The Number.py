print("GUESS THE NUMBER")

n = 50
no_of_guess = 1
print("Number of guess is limited to only 9 Times :  ")
while(no_of_guess<=9):
    guess_number = int(input("Guess the Number : "))
    if guess_number<50:
        print("You entered too low")
    elif guess_number>50:
        print("You enterd too high")
    else:
        print("You Won")
        print(no_of_guess,"No of Guess took to finish.")
        break
    print(9-no_of_guess,"No of Guesses left")
    no_of_guess = no_of_guess+1
if(no_of_guess>9):
    print("Game Over")