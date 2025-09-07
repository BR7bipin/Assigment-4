secret = 7
print("Welcome to the Guessing Game")

while True:
    guess = int(input("Enter a number (Enter -1 to QUIT): "))

    if guess == secret:
        print("🎉 Correct!")
        break
    elif guess < -1:
        print("Skipping Guess, Try Again")
        continue
    elif guess == -1:
        print("Quitting Game!")
        break
    else:
        print("Wrong Guess, Try Again")
